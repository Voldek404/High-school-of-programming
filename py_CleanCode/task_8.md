# Task 8. Константы

1)
```python
template = "1100" # TEMPLATE_TEST_7_AND_8

```
Дважды используется один и тот же шаблон для двух "родственных" тестов.
Это можно вынести в отдельный модуль с константами для улучшения структуры и читаемости кода.


2)
```python
if len(bitString) < 387840 # MIN_LENGTH_TEST_9

```
В соответствии с документацией университета, величина минимальной длины последовательности определена для каждого теста. Просто применение числового значения не совсем наглядно, а вынесение минимальной длины в константу делает более наглядным чтение кода.

3) 
```python
pValue_1 >= 0.01  # pValue_1 >= P_VALUE_THRESHOLD

```
Пороговое значение 0.01, используемое на протяжении всего кода, вполне уместно заменить на P_VALUE_THRESHOLD


4)
```python
byte_index >= 8192 # BUFFER_SIZE
```
Задачка из восьми, заданный размер буфера явно удобно задать константной для дальнейшего использование. Голое число смотрится не так наглядно


5)
```python
return 3.14 * self.radius ** 2 # return PI * self.radius ** 2
```
Ну и куда без классики


6)
```python
randomNumbers = [random.randint(0, 65535) # MAX_RANDOM_NUMBER = 65535 

```
Максимально значение для случайного числа, используемое при генерации случайных чисел

7)
```python
url = f"https://www.random.org/integers/?num={randomNumbersQRNG}&min=0&max=65535&col=1&base=10&format=plain&rnd=new"
        response = requests.get(url) # RANDOM_ORG_URL

```
Вынести в константы так же можно единственную в коде API- шку


8)
```python
 N # MIN_BITSTRING_LENGTH_4_BLOCK
```
 Кромы выделения переменной в константу дано более наглядное название, исключающее неверное применение


9)
```python
 prob_one_less_rank = 0.5776 # PROB_ONE_LESS_RANK
```
Переменная, не изменяющаяся в течение всего кода


10)
```python
 M = 32 # MATRIX_M 
```
Один из параметров размерности матрицы. Выделен в константу, назван наглядно


11)
```python
rank = np.sum(np.abs(np.diag(u)) > 1e-10) # Вместо 1e-10 можно использовать EPSILON
```
Числовое значение заменено на константу

12)
```python
 number > 10 ** 9 # number > INVARIANT_VALUE
```
 В отдельно константу выделен заданный верхний предел числового диапазона для проверки на инвариант вводящегося через пользовательский интерфейс значения