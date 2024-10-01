def bracketsGenerator(numberOfPairs):
    bracketCombinations = []
    initialState = ("", 0, 0)
    states = [initialState]
    while states:
        currentState, openCount, closeCount = states.pop()
        if openCount == numberOfPairs and closeCount == numberOfPairs:
            bracketCombinations.append(currentState)
            continue
        if openCount < numberOfPairs:
            states.append((currentState + "(", openCount + 1, closeCount))
        if closeCount < openCount:
            states.append((currentState + ")", openCount, closeCount + 1))
    return bracketCombinations
