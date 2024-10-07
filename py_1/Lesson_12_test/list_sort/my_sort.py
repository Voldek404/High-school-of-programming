import random
def list_sort( list10):
    i = 0
    while i < n - 1:
        m = i
        j = i + 1
        while j < n:
            if list10[j] < list10[m]:
                m = j
            j += 1
        list10[i], list10[m] = list10[m], list10[i]
        i += 1
    return list10
n = 10
list10 =[]
for i in range(n):
     list10.append(random.randint(1, 99))
print(list_sort(list10))