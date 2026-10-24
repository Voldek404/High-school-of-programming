# Задание №5

### Рефлексию решил вынести наверх по результатам выполнения задания: документирование классов/методов путем описания нахождения данного метода/класса в общей системе существенно улучшает читаемость кода, особенно если сразу в описании написать, где имеются usage данного метода/класса. Даже читая собственный код спустя месяц-два уже требуется время повспоминать, на что он завязан внутри программы.


Для выполнения задания выбран реализованный мной метод скорринга наличия возможной грубости (акустические признаки) в канале оператора

Отдельно в файле реализован класс `ONNXPipeline` с обвязкой в виде Аудио-утилит для работы с аудио + сама моделька в `.onnx`

```python
class ONNXPipeline:

    def __init__(
        self,
        rude_onnx_path="rude.onnx",
        sr=16000,
        full_call=False,
        client_is_target=False,
    ):

        self.sr = sr
        self.full_call = full_call
        self.client_is_target = client_is_target

        # ONNX sessions

        self.rude_session = ort.InferenceSession(
            rude_onnx_path, providers=["CPUExecutionProvider"]
        )

        self.true_threshold = 0.8
        self.doubt_threshold = 0.6

    # =====================================================
    # helpers
    # =====================================================

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def predict_rude(self, wav: np.ndarray) -> float:

        chunks = AudioUtils.sliding_windows(wav).numpy().astype(np.float32)

        logits = self.rude_session.run(None, {"audio": chunks})[0]

        return float(self._sigmoid(logits).item())

    # =====================================================
    # FILE PROCESSING
    # =====================================================

    def process_file(self, file) -> dict:
        file.seek(0)
        wav, _ = librosa.load(file, sr=self.sr, mono=True)
        rude_prob = self.predict_rude(wav)

        return {
            "status": (
                "rudeness_detected"
                if rude_prob >= self.true_threshold
                else "rudeness_not_detected"
            ),
            "rude_prob": rude_prob,
        }
```

Класс используется в основном пайплайне в соответствие с методом ниже

```python
pipeline = ONNXPipeline(str(MODEL_PATH))
```

```python
"""
ONNXPipeline входит в подсистему автоматического анализа разговоров и отвечает за определение вероятности грубости по аудио,
по дефолту это канал оператора.
Он получает отдельный аудиофайл от функции пакетной обработки и возвращает оценку наличия грубости в данном аудиофайле.
Эти результаты могут использоваться следующим компонентом для отбора разговоров на проверку.
Загрузка списка файлов и обработка ошибок отдельных записей выполняются внешней функцией _rudeness_score().
"""


def _rudeness_score(
    files: List[BytesIO],
    pipeline: ONNXPipeline,
) -> List[Optional[float]]:
    empty_files = [i for i, f in enumerate(files) if f.getbuffer().nbytes < 100]

    files = [f for i, f in enumerate(files) if i not in empty_files]

    rudeness_scores: List[Optional[float]] = []

    for f in files:
        try:
            result = pipeline.process_file(f)
            rudeness_scores.append(result["rude_prob"])
        except Exception:
            logging.exception("Rudeness inference failed")
            rudeness_scores.append(None)

    for i in empty_files[::-1]:
        rudeness_scores.insert(i, None)

    return rudeness_scores
```


### Создание автомобиля через веб-интерфейс



```python

"""Класс `ManagerVehicleCreateView` входит в подсистему управления автопарком и обеспечивает создание автомобиля менеджером через веб-интерфейс. После успешного создания инициирует Telegram-уведомление менеджеру. Ошибка уведомления не должна препятствовать созданию автомобиля.
"""
class ManagerVehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "authentication/vehicle_create.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_invalid(self, form):
        print("FORM INVALID")
        print(form.errors)

        return super().form_invalid(form)

    def form_valid(self, form):
        manager = self.request.user.managers

        print("ENTERPRISE:", form.instance.enterprise)

        # Критическая операция: автомобиль должен быть сохранён в БД.
        with transaction.atomic():
            response = super().form_valid(form)

        # Telegram — некритичная внешняя операция.
        # Ошибка или недоступность Telegram не влияет на создание автомобиля.
        try:
            from telegram_bot.models import TelegramProfile

            profile = TelegramProfile.objects.get(manager=manager)

            send_telegram_notification(
                telegram_id=profile.telegram_id,
                message=(
                    f"🚗 Автомобиль успешно создан\n\n"
                    f"Марка: {self.object.brand}\n"
                    f"Госномер: {self.object.plate_number}\n"
                    f"Цвет: {self.object.color}\n"
                    f"Дата выпуска: {self.object.prod_date}"
                )
            )

            print(
                f"Telegram notification sent: {profile.telegram_id}"
            )

        except TelegramProfile.DoesNotExist:
            print(
                f"У менеджера {manager.id} нет Telegram профиля"
            )

        except Exception as e:
            print(
                f"Ошибка отправки Telegram: {e}"
            )

        return response

### Подготовка аудиоданных для экспериментов

```python
    # Метод входит в подсистему подготовки аудиоданных для экспериментов.
    # Организует создание вариантов исходных записей с различными способами
    # обработки для последующего сравнения.
    # Результаты сохраняются отдельно по экспериментам с сохранением
    # относительной структуры входных файлов.
    # Преобразование аудио делегируется process_pipeline.
    # Ошибка отдельной обработки не останавливает остальные эксперименты.
    def enhance_directory(
        self,
        input_dir,
        output_dir,
    ):

        input_dir = Path(input_dir)
        output_dir = Path(output_dir)

        loudnorm_filter = (
            "loudnorm="
            "I=-16:"
            "LRA=11:"
            "TP=-1.5"
        )

        highpass_filter = (
            "highpass=f=80"
        )

        highpass_dynaudnorm_filter = (
            "highpass=f=80,"
            "dynaudnorm="
            "framelen=500:"
            "gausssize=31:"
            "peak=0.8:"
            "maxgain=20"
        )

        soft_compressor_filter = (
            "acompressor="
            "threshold=-20dB:"
            "ratio=3:"
            "attack=20:"
            "release=250:"
            "makeup=2"
        )

        highpass_compressor_dynaudnorm_filter = (
            "highpass=f=80,"
            "acompressor="
            "threshold=-20dB:"
            "ratio=3:"
            "attack=20:"
            "release=250:"
            "makeup=2,"
            "dynaudnorm="
            "framelen=500:"
            "gausssize=31:"
            "peak=0.8:"
            "maxgain=20"
        )

        volume6_dynaudnorm_filter = (
            "volume=6dB,"
            "dynaudnorm="
            "framelen=500:"
            "gausssize=31:"
            "peak=0.8:"
            "maxgain=20"
        )

        compressor_filter = (
            "acompressor="
            "threshold=0.1:"
            "ratio=3:"
            "attack=20:"
            "release=250:"
            "makeup=1"
        )

        dynaudnorm_filter = (
            "dynaudnorm="
            "framelen=500:"
            "gausssize=31:"
            "peak=0.8:"
            "maxgain=20"
        )

        experiments = [

            (
                "loudnorm",
                loudnorm_filter,
                False,
            ),

            (
                "highpass_dynaudnorm",
                highpass_dynaudnorm_filter,
                False,
            ),

            (
                "highpass_compressor_dynaudnorm",
                highpass_compressor_dynaudnorm_filter,
                False,
            ),

            (
                "soft_compressor",
                soft_compressor_filter,
                False,
            ),

            (
                "volume6db_dynaudnorm",
                volume6_dynaudnorm_filter,
                False,
            ),

            (
                "deepfilter",
                None,
                True,
            ),

            (
                "compressor_deepfilter",
                compressor_filter,
                True,
            ),

            (
                "dynaudnorm_deepfilter",
                dynaudnorm_filter,
                True,
            ),

            (
                "plus6db_deepfilter",
                "volume=6dB",
                True,
            ),

            (
                "dynaudnorm",
                dynaudnorm_filter,
                False,
            ),

            (
                "compressor",
                compressor_filter,
                False,
            ),
        ]

        wav_files = sorted(
            input_dir.rglob("*.wav")
        )

        print(
            f"Found WAV files: {len(wav_files)}"
        )

        for input_file in wav_files:

            relative = input_file.relative_to(
                input_dir
            )

            print(
                f"\nProcessing {relative}"
            )

            for (
                experiment_name,
                ffmpeg_filter,
                use_deepfilter,
            ) in experiments:

                output_file = (
                    output_dir
                    / experiment_name
                    / relative.parent
                    / (
                        relative.stem
                        + "_"
                        + experiment_name
                        + ".wav"
                    )
                )

                try:

                    print(
                        f"  -> {experiment_name}"
                    )

                    self.process_pipeline(
                        input_file=input_file,
                        output_file=output_file,
                        ffmpeg_filter=ffmpeg_filter,
                        use_deepfilter=use_deepfilter,
                    )

                except Exception as e:

                    print(
                        f"  ERROR ({experiment_name}): {e}"
                    )
```