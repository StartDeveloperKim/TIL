n=int(input())
drinks=list(map(int, input().split()))

drinks.sort(reverse=True)
ans=drinks[0]
for i in range(1, n):
    print(ans, drinks[i]/2)
    ans+=(drinks[i]/2)
print(ans)
