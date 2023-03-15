n, k=map(int, input().split())
coins=[int(input()) for _ in range(n)]

ans=0
for i in range(n-1, -1, -1):
    if k//coins[i]>0:
        ans+=k//coins[i]
        k%=coins[i]
print(ans)
