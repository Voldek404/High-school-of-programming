def recursion_second_max_helper(arrayOfNumbers, index, firstMaximum, secondMaximum, count):
    if arrayOfNumbers[index] > secondMaximum:
        secondMaximum = arrayOfNumbers[index]
    if secondMaximum > firstMaximum:
        firstMaximum, secondMaximum = secondMaximum, firstMaximum
    if index >= len(arrayOfNumbers) - 1:
        if len(arrayOfNumbers) == 1:
            return arrayOfNumbers[0]
        count += 1
        if count == 2:
            return secondMaximum
        firstMaximum = 0
        secondMaximum = 0
        index = 0
    return recursion_second_max_helper(arrayOfNumbers, index=index + 1, firstMaximum=firstMaximum,
                                       secondMaximum=secondMaximum, count=count)


def recursion_second_max(arrayOfNumbers):
    return recursion_second_max_helper(arrayOfNumbers, 0, 0, 0, 0)
