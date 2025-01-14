# Task 9. Типы данных

1)
```python
if response.status_code == 200 # SUCCESS_STATUS

```
Магическое число заменено на константу

2)
```python
bitString = ''.join(format(num, '016b') for num in randomNumbers) # BINARY_MODE

```
 Классификатор битности не является магической строкой, однако удобно вынести его в константу для изменения вне основного рабочего кода

3)
```python
 observedValue = abs(nth_PatrialSum) / (bitStringLength) ** 0.5
//
 try:
    if bitStringLength == 0:
        raise ValueError("Длина битовой строки  не должна быть равной нулю")
 except ValueError as e:
    print(f"Ошибка: {e}")
```
 Добавлено исключение для случаев с нулевой длиной строки. Пример указан справочно из кода стажировки, исключение нуля можно сделать в другом месте (генератор случайных чисел настроить не с "0", а с "1")

4)
```python
testConclusion = (pValue >= 0.01) 
//
testConclusion = pValue >= P_VALUE_THRESHOLD

```
Улучшена читаемость посредством умирания скобок, ведь переменная testСonclusion всегда булева

5)
```python
  if village.count(white_walker) >= 1 and village.index(white_walker) != 0 and village.index(white_walker) +3 != len(village)
// if white_walker in village:
       index = village.index(white_walker)
       if index != 0 and index + 3 != len(village)
```
Произведена оптимизация логического выражения, лишний вызов метода index упрощен

6)
```python


```

7)
```python


```

8)
```python


```

9)
```python


```

10)
```python


```

11)
```python


```

12)
```python


```

