class List2:
    def __init__(self, start, end, Numbers, numbersLimit):
        self.current = start
        self.end = end
        self.numbers = Numbers
        self.numbersLimit = numbersLimit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end or self.numbersLimit >= self.numbers:
            raise StopIteration
        else:
            self.current += 1
            self.numbersLimit += 1
            if self.numbersLimit >= self.numbers:
                self.numbersLimit = 0
                self.current = start
            return self.current - 1


end = float('inf')
Numbers = 10
numbersLimit = 0
start = 1
