class String:
    def __init__(self, content):
        self.content = content

    def ad_hoc(self):
        return len(self.content)


class List:
    def __init__(self, content):
        self.content = content

    def ad_hoc(self):
        return len(self.content)


class Tuple:
    def __init__(self, content):
        self.content = content

    def ad_hoc(self):
        return len(self.content)

#Далее наглядно показан основной принцип ad hoc полиморфизма, когда один и тот же метод c len()
# подходит для разных типов данных, в нашем случае str, tuple and list

tuple = Tuple({1, 23, 456})
string = String('fghjklvbnm')
list = List([1, 2, 3, 4, 5, 6, 7, 8, ])
print(tuple.ad_hoc())
print(string.ad_hoc())
print(list.ad_hoc())
