class Bag:

    def __init__(self, items=[]):
        self.bag_value = {}
        for item in items:
            self.bag_value[item] = self.bag_value.get(item, 0) + 1

    def count(self, item):
        if item in self.bag_value:
            return self.bag_value[item]
        else:
            return 0

    def add(self, new):
        self.bag_value[new] += 1

    def remove(self, item):
        if item in self.bag_value:
            if self.bag_value[item] == 1:
                del self.bag_value[item]
            else:
                self.bag_value[item] -= 1
        else:
            raise ValueError(str(item) + ' not in bag')

    def __repr__(self):
        return f"Bag({self.bag_value})"


