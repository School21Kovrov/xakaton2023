a,b,n,m = map(int,input().split())
l = max(n + (n - 1) * a, m + (m - 1) * b)
r = min(n + (n + 1) * a, m + (m + 1) * b)
if l <= r:
    print(l, r)
else:
    print(-1)
