def recursion_palindrome_factory():
    def recursion_palindrom(number, i):
        string = str(number)
        if len(string) // 2 <= i:
            return True
        if string[i] != string[-i - 1]:
            return False
        return recursion_palindrom(number, i + 1)
    
    return lambda number: recursion_palindrom(number, 0)

