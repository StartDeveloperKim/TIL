import sys
input=sys.stdin.readline

n=int(input())
distance=list(map(int, input().split()))
oil=list(map(int, input().split()))

price=oil[0]
ans=distance[0]*price
for i in range(1, n-1):
    if oil[i]<price:
        price=oil[i]
    ans+=price*distance[i]

print(ans)
