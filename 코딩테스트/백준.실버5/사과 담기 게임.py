n, m=map(int, input().split())
start, end=1, m
ans=0
j=int(input())
for _ in range(j):
    apple=int(input())
    if  start <= apple <= end:
        continue
    else:
        move=0
        if apple < start:
            move=apple-start
        else:
            move=apple-end
        ans+=abs(move)
        start+=move
        end+=move

print(ans)
