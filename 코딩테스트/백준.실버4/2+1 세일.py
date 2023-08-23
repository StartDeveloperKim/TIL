import sys
input=sys.stdin.readline

n=int(input())
prices=[int(input()) for _ in range(n)]
ans=0

prices.sort(reverse=True)

for i in range(0, n, 3):
    if i+1>=n:
        ans+=prices[i]
    else:
        ans+=(prices[i]+prices[i+1])
print(ans)
