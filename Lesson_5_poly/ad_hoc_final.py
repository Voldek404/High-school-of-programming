class Integer:
    def __init__(self, content):
        self.content = content

    def ad_hoc(self):
        return self.content/2
class List:
    def __init__(self, content):
        self.content = content

    def ad_hoc(self):
        return self.content*2

integer = Integer(2)
list = List(['2'])
print(integer.ad_hoc())
print(list.ad_hoc())