string = input()
dic=dict()
for s in string:
    if s not in dic.keys():
        dic[s]=1
    else:
        dic[s]+=1

odd=0
for k, v in dic.items():
    if v%2:
        odd+=1
    if odd>1:
        print("I'm Sorry Hansoo")
        exit()

ans=[]
temp=[]
for k, v in dic.items():
    if v%2:
        temp=[k]
        for _ in range(v-v//2-1):
            ans.append(k)
    else:
        for _ in range(v//2):
            ans.append(k)

ans.sort()
print(ans)
print(''.join(ans)+''.join(temp)+''.join(reversed(ans)))
    
