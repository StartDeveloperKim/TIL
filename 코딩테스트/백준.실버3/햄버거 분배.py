n, k=map(int, input().split())
location=list(input())

ans=0
for i in range(len(location)):
    if location[i]=='P':
        for j in range(max(i-k, 0), min(i+k+1, n)):
            if location[j]=='H':
                location[j]='X'
                ans+=1
                break
print(ans)


