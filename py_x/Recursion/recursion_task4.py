def recursion_palindrom(number,i=0):
    string = str(number)
    if len( string)//2 <= i:
        return True
    if  string[i] !=  string[-i-1]:
        return False
    return recursion_palindrom(number,i+1)

