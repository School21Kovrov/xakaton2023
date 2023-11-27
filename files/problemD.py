def summ(N):
    res = 0
    while N > 0:
        res += N % 10
        N //= 10
    return res
print(summ(int(input())))
