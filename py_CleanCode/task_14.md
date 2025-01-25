# Task 14. Комментарии

3.1. Уместные комментарии

1) Есть три функции, для которых хотелось бы дать комментарий, но лучше будет просто индикатив переименовать
```python
def getRandomNumbers(randomNumbersQRNG: int)/// def getRandomNumbersApi # функция для получения данных по API

getRandomNumbersLocal(randomNumbersLocal: int) /// def getRandomNumbersFromLib # функция для получения данных из встроенной библиотеки Питона

def getRandomNumbersUser(dataNumbers: str) /// def getRandomNumbersFromFile # функция для получения данных из файла локально

```

2) Специализированный комментарий для выбора размера блока, в принципе тяжело переделать код, чтобы описать данную рекомендацию
```python
blockSize = bitStringLength // 10
numberOfBlocks = 10. #The blockSize  should be selected such that blockSize  ≥ 20, blockSize  > .01 bitStringLength and numberOfBlocks  < 100. 

```

3)
```python


```

4)
```python


```

5)
```python


```

6)
```python


```

7)
```python


```

3.2. Неуместные комментарии

1) Неуместный комментарий про подсчет факториала. Название переменной в целом сама за себя говорит, как и применяемый цикл
```python
or i in range(1, N + 1):
        factorial *= i  # calculating factorial

```

2) Абсолютно лишний комментарий, ничего из себя не представляющий. Даже код не нуждается в правке
```python
training_space = []  # forming a training space

```

3)
```python


```

4)
```python


```

5)
```python


```