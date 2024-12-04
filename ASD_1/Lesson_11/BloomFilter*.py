from BloomFilter import BloomFilter

def bloomFiltersIntersection(str1,str2):
    firstFilter = BloomFilter()
    secondFilter = BloomFilter()
    finalFilter = BloomFilter()
    numberOfHashFoos = 4
    for j in range(numberOfHashFoos):
        finalFilter.bit_list  |= getattr(firstFilter, f"hash{j + 1}")(str1)
        finalFilter.bit_list  |= getattr(secondFilter, f"hash{j + 1}")(str2)
    return finalFilter
