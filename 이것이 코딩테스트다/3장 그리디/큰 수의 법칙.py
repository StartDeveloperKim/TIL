n, m, k=map(int, input().split())
numbers=list(map(int, input().split()))
ans=0

numbers.sort(reverse=True)
max1, max2=numbers[0], numbers[1]
cnt=0
for _ in range(m):
    if cnt!=k:
        ans+=max1
    else:
        ans+=max2
        cnt=0
    cnt+=1
print(ans)
    
