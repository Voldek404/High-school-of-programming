def long_process(id, n):
    summa = 0
    for x in range(n):
        summa += x + 1
        print(id, summa)
        if x < n - 1:
            yield
        else:
            yield summa


generatorList = [10, 20, 30, 40, 50, 60, 70, 80]
resultDict = {}
expressions = []
for i in range(1, len(generatorList) + 1):
    resultDict[f'id{i}'] = None
keys = list(resultDict.keys())
print(type(keys))
n = 0
for i in generatorList:
    expressions.append(long_process(keys[n], i))
    n += 1
for i in range(max(generatorList)):
    for idx, gen in enumerate(expressions):
        key = keys[idx]
        if resultDict[key] is None:
            resultDict[key] = next(gen)
print(expressions)
print(resultDict)
