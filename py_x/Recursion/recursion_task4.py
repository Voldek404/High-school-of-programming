def recursion_palindrom(number, i):
    string = str(number)
    if len(string) // 2 <= i:  
        return True
    if string[i] != string[-i - 1]:  
        return False
    return recursion_palindrom(number, i + 1)  

def recursion_palindrome_factory():
    return recursion_palindrom(number, 0)


