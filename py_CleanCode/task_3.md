# Task 3

## 7.1 корректные наименования для нулевых переменных

1) covered - is_covered
// Переменная не подразумевала однозначно true or false

2) flag - is_recursive_call
// переменная flag должна была управлять рекурсивным вызовом. True - производство рекурсивного вызова Задача из py_1 на работу с каталогами

3) result - is_match
// переменная из задачи про танковый раш из 28 задач. Сама по себе переменная result абсолютно ни о чем не говорит. Полезно возвращаться к своему коду спустя время

4) rot_flag - is_rot 
// пример из чужого кода 

5) flag - is_all_positive
// пример из чужого кода, где флаг использовался для цикла while, функционирующего пока числа положительные




## 7.2 стандартные для булевых переменных наименования

1) is_match - success
// условное совпадение/попадание явно можно заменить стандартным термином

2) result - found
// из задачи про белых ходоков, где необходимо было вывести факт обнаружения



## 7.3 - наглядное обозначение переменных- счетчиков

1) for char in str_obj
// перебор символов в объекте типа строки

2) for index in list_obj
// случай, когда переменная счетчика используется вне итераций

3) for _ in range
// для отображения "безразличия" к переменной счетчика ( в случае нескольких циклов)



## 7.4 пары слов - антонимы

1) cumulative_sum_straight - cumulative_sum_reversed
// прямая (оригинальная) кумулятивная сумма и обратная

2) left_edge - right_edge
// крайний левый и крайний правый пределы

3) p_value_forward - p_value_backward
// метрики для определения "случайности" Битовой последовательности



## 7.5 Временные переменные
1) https://github.com/Voldek404/Internship/blob/74728ce712de14cb5733494e2aaa41e22ffaf973/task3_pumpDemand.py#L23\

//Временная переменная initial_demand создавалась для отделения процесса от общей мощности \total_capacity, однако после проведенного анализа стало ясно, что переменная целиком лишняя

2) temp - temporary_list, temporary_string

// чаще всего временные переменные в моем коде именовались просто как temp, что было не совсем наглядно

3) https://github.com/Voldek404/High-school-of-programming/blob/e47aaa882aded2d41c745902b2396a29082a4cb2/py_28tasks/task3.py#L7\

// еще одна лишняя временная переменная а1. Можно обойтись без нее
training_space = [] \
for i in range(1, N + 1):\
    training_space.append([0] * M)

