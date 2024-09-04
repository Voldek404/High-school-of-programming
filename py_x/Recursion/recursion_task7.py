def recursion_second_max_helper(arrayOfNumbers, index, firstMaximum, secondMaximum):
    if index >= len(arrayOfNumbers):
        return secondMaximum
    current = arrayOfNumbers[index]
    if current >=firstMaximum:
        secondMaximum = firstMaximum
        firstMaximum = current
    elif current >= secondMaximum:
        secondMaximum = current
    return recursion_second_max_helper(arrayOfNumbers, index + 1, firstMaximum, secondMaximum)


def recursion_second_max(arrayOfNumbers):
    if len(arrayOfNumbers) < 2:
        raise ValueError("Массив должен содержать минимум два элемента")
    if arrayOfNumbers[0] >= arrayOfNumbers[1]:
        firstMaximum, secondMaximum = arrayOfNumbers[0], arrayOfNumbers[1]
    elif arrayOfNumbers[0] <= arrayOfNumbers[1]:
        firstMaximum, secondMaximum = arrayOfNumbers[1], arrayOfNumbers[0]
    return recursion_second_max_helper(arrayOfNumbers, 2, firstMaximum, secondMaximum)
