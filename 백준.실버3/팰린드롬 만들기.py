## 1. 주어진 문자열의 각 알파벳 개수를 샌다.
## 2. 알파벳 개수 중 홀수 개수가 2개이상이면 팰린드롬 수를 만들지 못한다.
## 3. 짝수 개수의 알파벳은 나누기 2한 개수만큼 정답 리스트에 넣어준다.
## 4. 홀 수 개수의 경우 한개를 빼고 나머지 개수를 절반을 정답 리스트에 넣는다.
## 5. 정답 리스트 + 홀수알파벳 하나 + 거꾸로만든 정답리스트

string = input()
dic=dict()
for s in string:
    if s not in dic.keys():
        dic[s]=1
    else:
        dic[s]+=1

odd=0
ans=[]
temp=[]
for k, v in dic.items():
    if v%2:
        odd+=1
        temp=[k]
        for _ in range(v-v//2-1):
            ans.append(k)
    else:
        for _ in range(v//2):
            ans.append(k)
    
if odd>1:
    print("I'm Sorry Hansoo")
else:
    ans.sort()
    print(''.join(ans)+''.join(temp)+''.join(reversed(ans)))
    
