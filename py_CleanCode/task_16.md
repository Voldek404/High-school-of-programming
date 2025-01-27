# Task 16. Плохие комментарии

1) Лишний комментарий

```python
first_digit = factorial // 10 ** (len(str(factorial)) - 1)  # dividing factorial

```

2) В соответствии с 12ым пунктом - использование названия функции делает комментарий избыточным

```python
def clear_clipboard():
    pyperclip.copy("")  # Очищаем буфер обмена

```

3)  В соответствии с 12ым пунктом - использование названия функции делает комментарий избыточным

```python
def periodic_clear_clipboard():
    global last_clipboard
    last_clipboard = ""
    while True:
        time.sleep(1)  # Очищаем буфер обмена каждую секунду
        clear_clipboard()

```

4) В соответствии с 12ым пунктом - использование названия функции делает комментарий избыточным

```python
def clipboard_monitor():
    while True:
        time.sleep(0.1)  # Проверяем буфер обмена каждые 0.1 секунды
        check_clipboard()

```

5) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
result_label.config(text=result, fg="white")  # Показать результат

```

6) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
# Создание основного окна
root = tk.Tk()
root.title("Число сорок прописью")
root.configure(bg="#121400")

```

7) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
# Настройка шрифта
font_title = tk.font.Font(family="Times New Roman", size=24, weight="bold")
font_result = tk.font.Font(family="Times New Roman", size=18, weight="bold")

```

8) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
root.bind("<ButtonPress>", hide_text)  # Скрытие текста при нажатии кнопок мыши

```

9) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
# Создаем 8 насосов с различными параметрами
pumps = [generate_pump(i) for i in range(1, 8)]

```

10) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
for i in range(100):  # 100 шагов (например, для 100 минут или секунд)

```

11) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
logging.info(f"Получен новый спрос: {demand} м³/ч")  # Логируем текущий спрос

```

12) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
# Создаем график
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_ylim(0, total_capacity)

```

13) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
# Создаем поле для вывода логов
log_text = ax.text(0.1, 0.95, '', transform=ax.transAxes, fontsize=10, verticalalignment='top', horizontalalignment='left')

```

14) Лишний комментарий в соответствии с 12ым пунктом рекомендаций


```python
 global bars  # Используем глобальную переменную для bars

```

15) Лишний комментарий в соответствии с 12ым пунктом рекомендаций

```python
 # Обновляем линию суммарного потребления мощности
    line.set_data(range(len(selected_pumps)), [total_power_consumption] * len(selected_pumps))

```

