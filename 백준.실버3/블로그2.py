n=int(input())
problems=input()

ans={'B':0, 'R':0}
ans[problems[0]]+=1
for i in range(1, n):
    if problems[i]!=problems[i-1]:
        ans[problems[i]]+=1
print(min(ans['B'], ans['R'])+1)
