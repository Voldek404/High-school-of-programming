def TransformTransform(A: list, N: int) -> bool:
    B = []
    if N <= 1:
        return False
    for i in range(N):
        for j in range(N - i):  
            B.append(max(A[j:j + i + 1])) 
    C = []
    for i in range(len(B)):
        for j in range(len(B) - i): 
            C.append(max(B[j:j + i + 1])) 
    return sum(C) % 2 == 0
