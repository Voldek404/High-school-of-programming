# Task 11. Время жизни переменных


1) Класс переименован в соответствии с рекомендациями, выполнено корректное наследованние (введен конструктор), публичные атрибуты, которые не должны меняться никогда - заменены на приватные
```python
class CurrentTransformer:
    tip = ' ТЛМ - 10'
    nominal_current_A = 5
    precision_class = "0.5S"
    nominal_load_tt_VA = 5
    mpi_years = 8
    poveren = True
///
class CurrentTransformer:
    def __init__(self, tip='ТЛМ - 10', nominal_current_A=5, precision_class="0.5S", 
                 nominal_load_tt_VA=5, mpi_years=8, poveren=True):
        self.__tip = tip  # Приватный атрибут
        self.__nominal_current_A = nominal_current_A  
        self.__precision_class = precision_class  
        self.__nominal_load_tt_VA = nominal_load_tt_VA 
        self.__mpi_years = mpi_years  
        self.__poveren = poveren  

```