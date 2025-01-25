# Task 14. Комментарии

3.1. Уместные комментарии

1) Есть три функции, для которых хотелось бы дать комментарий, но лучше будет просто индикатив переименовать

```python
def getRandomNumbers(randomNumbersQRNG: int)/// def getRandomNumbersApi # функция для получения данных по API

def getRandomNumbersLocal(randomNumbersLocal: int) /// def getRandomNumbersFromLib # функция для получения 
#данных из встроенной библиотеки Питона

def getRandomNumbersUser(dataNumbers: str) /// def getRandomNumbersFromFile # функция для получения данных 
#из файла локально

```

2) Специализированный комментарий для выбора размера блока, в принципе тяжело переделать код, чтобы описать данную рекомендацию

```python
blockSize = bitStringLength ///  10
numberOfBlocks = 10. #The blockSize  should be selected such that 
#blockSize  ≥ 20, blockSize  > .01 bitStringLength and numberOfBlocks  < 100. 

```

3) Еще один специализированный комментарий, который невозможно избежать. В документации, конечно, все доступно расписано, но пока найдешь

```python 
L = 7 # L should be chosen so that 6 ≤ L ≤ 16

```

4) Специализированный комментарий

```python
M = 500 # 500≤ M ≤ 5000, and N ≥ 200 for the χ result to be valid

```

5) Специализированный комментарий
```python
m = templateLength #It is recommended that m = 9 or m = 10 be specified to obtain meaningful results

```

6) Специализированный комментарий
```python
N = 10 # N should be chosen such that N ≤ 100 to be assured that the
P-values are valid

```

7) Специализированный комментарий
```python
Q = 1280 # Q should be chosen so that Q = 10 • 2**L

```
Таким образом, можно констатировать, что в большинстве случае написания моего немногочисленного кода - практически везде можно обойтись без комментариев с помощью наглядных названий функций и переменных. Однако спец параметры, размерность которых выбирается в соответствие со строгими рекомендациями, следует в обязательном порядке комментировать для наглядности и экономии времени, если вдруг понадобится потом вспомнить ( подобное замечание мне сделали на стажировке).


3.2. Неуместные комментарии. В принципе по мере прохождения курса мало комментировал, следуя концепции CleanCode

1) Неуместный комментарий про подсчет факториала. Название переменной в целом сама за себя говорит, как и применяемый цикл
```python
or i in range(1, N + 1):
        factorial *= i  # calculating factorial

```

2) Абсолютно лишний комментарий, ничего из себя не представляющий. Даже код не нуждается в правке
```python
training_space = []  # forming a training space

```
