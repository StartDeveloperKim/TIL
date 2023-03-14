import sys
input=sys.stdin.readline

n=int(input())
tips=[int(input()) for _ in range(n)]
tips.sort(reverse=True)

ans=0
for i, tip in enumerate(tips):
    temp=tip-i
    if temp>0:
        ans+=temp
print(ans)
