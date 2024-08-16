def SherlockValidString(s: str) -> bool:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    freq_count = {}
    for count in char_count.values():
        freq_count[count] = freq_count.get(count, 0) + 1
    if len(freq_count) == 1:
        return True
    if len(freq_count) == 2:
        min_freq = min(freq_count)
        max_freq = max(freq_count)
        if max_freq == min_freq + 1 and freq_count[max_freq] == 1:
            return True
        if min_freq == 1 and freq_count[min_freq] == 1:
            return True
    return False
