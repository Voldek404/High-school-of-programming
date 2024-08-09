def LineAnalysis(line: str) -> bool:
    length = len(line)
    if length % 2 == 0:
        first_half = line[:length // 2]
        second_half = line[length // 2:]
        reversed_second_half = second_half[::-1]
    else:
        first_half = line[:length // 2 + 1]
        second_half = line[length // 2:length]
        reversed_second_half = second_half[::-1]
    return first_half == reversed_second_half
