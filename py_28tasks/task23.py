def array_to_string(tree):
    return ''.join(tree)

def get_plus_indices(s):
    return {i: 1 for i, char in enumerate(s) if char == '+'}

def TreeOfLife(H: int, W: int, N: int, tree: list[str]) -> list[str]:
    s = array_to_string(tree)
    plus_indices = get_plus_indices(s)

    for year in range(0, N):
        if year % 2 == 0:  
            new_s = list(s)
            for i in range(len(s)):
                if s[i] == '.':
                    new_s[i] = '+'
                    plus_indices[i] = 1
                elif s[i] == '+':
                    plus_indices[i] += 1
            s = ''.join(new_s)
        else:
            for i in plus_indices:
                plus_indices[i] += 1


        to_dot = set()
        for i, value in plus_indices.items():
            if value >= 3:
                to_dot.add(i)
                if i % W != 0:
                    to_dot.add(i - 1)
                if (i + 1) % W != 0:
                    to_dot.add(i + 1)
                if i - W >= 0:
                    to_dot.add(i - W)
                if i + W < W * H:
                    to_dot.add(i + W)

        new_s = list(s)
        for i in to_dot:
            new_s[i] = '.'
            if i in plus_indices:
                del plus_indices[i]

        s = ''.join(new_s)

    return [s[i:i + W] for i in range(0, len(s), W)]
