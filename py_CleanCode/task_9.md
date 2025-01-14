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
Улучшена читаемость посредством удаления скобок, ведь переменная testСonclusion всегда булева

5)

```python
result1 = current_string[index] if 0 <= index < len(current_string) else ''
//
result2 = current_string[index:index+1]

```
Более лаконичная проверка вхождения индекса в строку


6)

```python
def array_to_string(tree):
    return ''.join(tree)
//
def array_to_string(tree):
    tree_copy = tree[:] 
    return ''.join(tree_copy)
```
 Устранено изменение исходной переменной, вместо этого работа производится с ее копией

7)

```python
 result.append(int(str(data[i]), 8))
//
 result.append(int(data[i], 8)) 

```
Убрано лишнее преобразование типов, которое не было необходимым в рамках задачи

8)

```python
perms = sorted(set(''.join(p) for p in permutations(input)))
//
perms = set(''.join(p) for p in permutations(input_str))
perms = sorted(perms)

```
Выполнено более наглядное преобразование, путем различения выражения на две части

9)

```python
   flag = 0
    raw_price = sorted(price, reverse=True)
    if N >= 3:
        flag = True
//
    isDiscount = False

```
 Переменная изначально введена булевой, во избежание преобразования типов на ровном месте + изменено название самой переменной в соответствие с ранее изученными рекомендациями

10)

```python

if hits[i] == 6 and hits[i + 1] == 1 or hits[i + 1] == 6 and hits[i] == 1:
    hits_sum += 1
//
if {hits[i], hits[i + 1]} == {1, 6}:  
    hits_sum += 1

```
 Упрощение при помощи множеств, где обе комбинации успешно проверятся без лишних логических проверок

11)

```python
abs(hits[i] - hits[i + 1]) == 4 or abs(hits[i] - hits[i + 1]) == 2 or abs(hits[i] - hits[i + 1]) == 7 or abs(hits[i] - hits[i + 1]) == 5
//
if abs(hits[i] - hits[i + 1]) in {4, 2, 7, 5}

```
 Проверка с помощью множеств при сравнении числа с множеством, существенное укорочение длины записи

12)

```python
if village.count(white_walker) >= 1 and village.index(white_walker) != 0 and village.index(white_walker) +3 != len(village) :
//
if village.count(white_walker) >= 1 and white_walker in village[1:-3]

```
Выполнено укорачивание проверки на вхождение при помощи срезов. Также убраны лишние вызовы

