N = map(int, input())
A = []
A = list(map(int, input().split()))

res = 20000000000
for i in range (1 << (N-1)):
    xored =0
    ored = 0
    for j in range (N+1):
        if (j < n) ored |= A[j]
        if (j == N or (i>>j & 1)) xored ^= ored, ored =0
    res = min(res,xored)

print(res)
