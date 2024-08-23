def recursion_palindrom(number):
    string = str(number)
    if len( string) <= 1:
        return True
    if  string[0] !=  string[-1]:
        return False
    return recursion_palindrom(string[1:-1])

