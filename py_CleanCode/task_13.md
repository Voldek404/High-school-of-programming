# Task 13. Работа с массивами

1) Перебор с прямым доступам к элементам индекса по спискам заменен использованием функции zip, благо списки одинаковой длины. В целом также реализована рекомендации ранее пройденного занятия, где проход по элементам массива предлагался с помощью наглядного названия минимальной единицы такого массива, не просто буквенной переменной

```python
for i in range(0, N):
    if football_list[i] != football_list_sorted[i]:
///
for item, sorted_item in zip(football_list, football_list_sorted):
    if item != sorted_item   

```

2) Исключен доступ по индексам. Минимальный элемент назван в соответсвии с рекомендацией. Разительно улучшилась читаемость

```python
for i in range(0, len(S2)):
    map_2_string += S2[i]
///
for element in S2:
    map_2_string += element

```

3) При данной записи можно избежать обращения к элементам списка по индексу посредством использования функции enumarate, возвращающей кортеж их пронумерованных элементов списка, в связи с чем обращение идет через номер элемента с последующим переключением двери. На мой взгляд данная конструкция безопаснее

```python
for i in range(k):
    if doors_list[i] == 0:
        doors_list[i] = 1
///
for i, element in enumerate(doors_list[:k]):
    if element == 0:
        doors_list[i] = 1

```

4) Убрана лишняя логика с break - ограничен проход по range до N - 1, таким образом более внимательный подход к границам списка. Более аккуратно выполнен доступ по индексам - во избежание ошибок при копипасте текущий и следующий элементы получили собственное обозначение. Так же реализовано множество для более лаконичной проверки условий

```python
 for i in range(N):
        if i + 1 == N:
            break
        if hits[i] == 6 and hits[i + 1] == 1 or hits[i + 1] == 6 and hits[i] == 1:
            hits_sum += 1
        elif hits[i] == 7 and hits[i + 1] == 3 or hits[i + 1] == 7 and hits[i] == 3:
            hits_sum += 1
        elif abs(hits[i] - hits[i + 1]) == 4 or abs(hits[i] - hits[i + 1]) == 2 or abs(hits[i] - hits[i + 1]) == 7 or abs(
                hits[i] - hits[i + 1]) == 5:
            hits_sum += 2 ** 0.5
        else:
            hits_sum += 1
///
for i in range(N - 1):
    current_hit = hits[i]
    next_hit = hits[i + 1]
    if (current_hit == 6 and next_hit == 1) or (current_hit == 1 and next_hit == 6):
        hits_sum += 1
    elif (current_hit == 7 and next_hit == 3) or (current_hit == 3 and next_hit == 7):
        hits_sum += 1
    elif abs(current_hit - next_hit) in {4, 2, 7, 5}:  
        hits_sum += 2 ** 0.5
    else:
        hits_sum += 1


```

5)

```python

```