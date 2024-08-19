def TransformTransform(A: list, N: int) -> bool:
    B = []
    if N <= 1:
        return False
    for i in range(0, N - 1):
        for j in range(i, N):  
            B.append(max(A[i:j + 1])) 
    C = []
    for i in range(0, len(B) - 1):
        for j in range(i, len(B)): 
            C.append(max(B[i:j + 1])) 
    return sum(C) % 2 == 0  
