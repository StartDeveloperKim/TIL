n=int(input())
ans=0
five=n//5
if n>=5:
    while five>=0:
        temp=n-(5*five)
        if temp%2==0:
            ans+=five+(temp/2)
            break
        else:
            five-=1
    print(int(ans))
else:
    if n%2==0:
        print(n//2)
    else:
        print(-1)
