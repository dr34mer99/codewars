def printKPFNums(A, B, K):
    prime = []
    p_factors = [0] * (B + 1)
    for p in range(2, B + 1):
        if p_factors[p] == 0:
            for i in range(p, B + 1, p):
                p_factors[i] = p_factors[i] + 1
    for i in range(A, B + 1):
        if p_factors[i] == K:
            prime.append(i)
    return prime

print(printKPFNums(10,23,2))

