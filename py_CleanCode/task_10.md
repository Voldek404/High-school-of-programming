# Task 10. Работа с переменными

1) Счетчик суммы определен сильно раньше цикла, что делает код не совсем наглядным. Лучше определить его непосредственно перед циклом, в соответствии с рекомендациями

```python
    toner_sum = 0
    sample_dict = {
        ' ': 0, '!': 9, '"': 6, '#': 24, '$': 29, '%': 22, '&': 24, "'": 3, '(': 12, ')': 12, '*': 17,
        '+': 13, ',': 7, '-': 7, '.': 4, '/': 10, '0': 22, '1': 19, '2': 22, '3': 23, '4': 21, '5': 27,
        '6': 26, '7': 16, '8': 23, '9': 26, ':': 8, ';': 11, '<': 10, '=': 14, '>': 10, '?': 15, '@': 32,
        'A': 24, 'B': 29, 'C': 20, 'D': 26, 'E': 26, 'F': 20, 'G': 25, 'H': 25, 'I': 18, 'J': 18, 'K': 21,
    }
    for i in Line:
       if i in sample_dict:
          toner_sum += sample_dict[i]
///
    toner_sum = 0
    for i in Line:
       if i in sample_dict:
          toner_sum += sample_dict[i]

```

2) Перменная счетчика неверно выполнена одинаковой для двух разных циклов. Корректнее использовать разное обозначение, а так же назвать счетчик в соответсвии с минимальной единицей перебираемой структуры данных
```python
 for i, value in plus_indices.items():
            if value >= 3:

        new_s = list(s)
        for i in to_dot:
            new_s[i] = '.'
            if i in plus_indices:
///
 for dot in to_dot:

```

3) Стилистически неверное в квадрате испольщование переменных счетчика. Введены дополнительные переменные
```python
    for i in range(N):
        for j in range(N - i):  
            B.append(max(A[j:j + i + 1])) 
    C = []
    for i in range(len(B)):
        for j in range(len(B) - i): 
            C.append(max(B[j:j + i + 1])) 
///
    for i in range(N):
        for j in range(N - i):  
            B.append(max(A[j:j + i + 1])) 
    C = []
    for k in range(len(B)):
        for l in range(len(B) - k): 
            C.append(max(B[l:l + k + 1])) 

```

4) Внутри метода изменяется переменная, которая подается в качестве аргумента этому самому методу - плохой стиль. Будем работать с ее копией
```python
def TheRabbitsFoot(s, encode):
    if encode:
        s = s.replace(' ', '')
///
def TheRabbitsFoot(s, encode):
    if encode:
        s_replaced = s.replace(' ', '')
```

5) Добавлена обработка инварианта для программы с пользровательским интерфейсом ввода числа, по условиям задачи целого
```python
 if number < 0 or number > 10 ** 9 or isinstance(number, float):
        return "Invariant Value"

```

6)Добавлена обработка превышения результата запроса, считай инвариант, при запросе даннх через apiю До этого код обрабатывал лишь код 200 и все, кроме него
```python
  except requests.Timeout:
        print("Ошибка: запрос превысил время ожидания.")
        return None, None, None

```

7) Добавлена проверка на инвариант в части принадлежности числа заданному числовому диапазону
```python
def to_16bit_binary(num):
    if num < 0:
//
def to_16bit_binary(num):
    if not (-32768 <= num <= 65535):
        raise ValueError(f"Число {num} выходит за допустимый диапазон для 16-битного представления")
    
    if num < 0:
```

8) Введение подстраховки от деления на очень малое значение ( рекомендация документации на тесты)
```python
chiSquare += (F[i] - expected_counts[i]) ** 2 / (
            expected_counts[i] + 1e-10)
//
if expected_counts[i] > 1e-10:
    chiSquare += (F[i] - expected_counts[i]) ** 2 / expected_counts[i]
else:
    chiSquare += (F[i] - expected_counts[i]) ** 2 / 1e-10

```

9)Введение мер безопасности при вычислении метрики, во избежание абсолютного нуля
```python
pValue = sp.gammaincc(K / 2, chiSquare / 2)
//
pValue = sp.gammaincc(K / 2, max(chiSquare / 2, 1e-10))

```

10)Лишнее определение переменной initial_demand, фактически дублирует существующую переменную
```python  
total_capacity = sum([pump['capacity'] for pump in pumps])
initial_demand = total_capacity
queue = deque()
for i in range(100): 
    demand_random_changer = np.random.choice(np.arange(0, 1.0, 0.05))
    demand = demand_random_changer *  initial_demand  
    if total_capacity < demand:
        continue
    elif demand == 0:
        continue
    queue.append(demand)
total_capacity = sum([pump['capacity'] for pump in pumps])
///
queue = deque()
for i in range(100):  # 100 шагов 
    demand_random_changer = np.random.choice(np.arange(0, 1.0, 0.05))
    demand = demand_random_changer * total_capacity  
    if total_capacity < demand:
        continue
    elif demand == 0:
        continue
    queue.append(demand)
///
```


11)Завершение работы с переменной
```python
s = ''.join(new_s)
///
s = ''.join(new_s)
new_s = None

```

12)Для лучшей читаемости переприсваивание переставлено местами
```python
if len(string_2) > len(string_1):
    string_2, string_1 = string_1, string_2
//
if len(string_2) > len(string_1):  
    string_1, string_2 = string_2, string_1 

```
13)Обработка завершения работы с переменной, возвращаем ноль вместо пустой строки
```python
result = result.lstrip('0')
//
result = result.lstrip('0') 
if result == '':  
    result = '0'

```

14)Добавлена проверка на инвариант в части подачи пустой строки
```python
def WordSearch(length, input_string, subs):
    search_list = []
    splitted_string = input_string.split()
//
if not input_string.strip():
    raise ValueError("Input string cannot be empty or only contain spaces.")

```

15)Проверка на инвариант, при попытке ввести в строку инпута не числовые символы
```python
if not input_string.isdigit():
        raise ValueError(f"Invalid input: '{input_string}' contains non-numeric characters.")

```

