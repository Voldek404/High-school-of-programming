# Task 15. Правильные комментарии

1) Представление намерений. В целом, на мой взгляд, переименование в demand_queue тоже неплохо выглядит
```python
# Очередь для моделирования спроса (с диапазоном изменения)
queue = deque()

```

2) Предупреждение о последствиях

```python
# Очень долгое выполнение. 
# На длинных выборках (свыше 1 млн битов)
# Лучше выполнять тесты по одному
def run_all_tests(self)

```

3) Информативный комментарий

```python
# Разбиваем данные на блоки
chunks = [dataNumbers[i:i + chunk_size] for i in range(0, len(dataNumbers), chunk_size)]

```

4) Представление намерений

```python
demand = demand_random_changer *  initial_demand  # имитация изменения спроса

```

5) Информативный комментарий

```python
demand_random_changer = np.random.choice(np.arange(0, 1.0, 0.05)) # задаем вариативность спроса от нуля до 100 процентов с шагом в пять процентов

```
6) Усиление / предупреждение о последствиях

```python
response = requests.get(url) # API выдает результат с тайм-аутом в 3 минут
# при более частых запросах не пугайся, это не зависание

```

7) Информативный комментарий

```python
# Функция для спирального вращения матрицы п часовой стрелке
def MatrixTurn(Matrix, M, N, T) -> None: 

```

8) Информативный комментарий

```python
# вспомогательная функция во избежание 
#использования дефолтных параметров в основной функции
def massdriver_helper(activate: list, index: int, activate_dict) -> int: 

```

9) Информативный комментарий

```python
    # Пропорции для блока длиной 8, 128 и 100000 бит взяты из официальной документации
    if blockSize == 8:
        proportionOf1 = [0.2148, 0.3672, 0.2305, 0.1875]
    elif blockSize == 128:
        proportionOf1 = [0.1174, 0.2430, 0.2493, 0.1752, 0.1027, 0.1124]
    elif blockSize == 100000:
        proportionOf1 = [0.00882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]

```

10) Информативный комментарий, касательно предназначения данного теста

```python
def universalStatisticalTest_9(bitString: str, bitStringLength: int):
"""The purpose of the test is to detect whether or not the sequence can be
significantly compressed without loss of information."""

```

11) Информативный комментарий, без него сложно визуально понять

```python
# Создаём словарь для подсчёта всех возможных бинарных строк длины m.
# Ключи — бинарные строки длины m (например, '00', '01' для m=2),
# значения — количество их вхождений, инициализированное нулями.
patternCount = {bin(i)[2:].zfill(m): 0 for i in range(2 ** m)}

```

12) Информативный комментарий, раскрывающий смысл функции, хоть из названия и ясно, что она определяет ранг матрицы.

```python
# Вычисляет ранг бинарной матрицы с использованием LU-разложения.
def rank(binary_matrix):
        _, u = lu(binary_matrix, permute_l=True)
        rank = np.sum(np.abs(np.diag(u)) > 1e-10)
        return rank

```
