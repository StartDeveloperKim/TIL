n=int(input())
distance=list(map(int, input().split()))
oil=list(map(int, input().split()))

price=oil[0]
ans=price*distance[0]

for i in range(1, n-1):
    print(ans)
    if oil[i]<price:
        price=oil[i]
    ans+=(price*distance[i])
print(ans)
        
