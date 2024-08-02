def MassVote(candidates_number, votes_array):
    max_number = 0
    max_value = max(votes_array)
    max_share = round(((max_value / sum(votes_array))* 100),3)
    result = ''
    for i in range(0, candidates_number):
        if max_value == votes_array[i]:
            max_number += 1
    if max_number >= 2:
        result = "no winner"
    elif max_share > 50:
        result = f"majority winner {votes_array.index(max_value) + 1}"
    elif max_share <= 50:
        result = f"minority winner {votes_array.index(max_value) + 1}"
    return result
