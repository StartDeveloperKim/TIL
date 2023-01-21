## 알고리즘
## 1. '-'를 기준으로 수를 나눈다. -> '+'가 있는 수식에 괄호를 씌우는 효과
## 2. 나눠진 수식을 '+'로 나누고 합하여 result 리스트에 넣는다.
## 3. result 에는 '+' 연산자가 있는 수식과 일반 수가 연산된 결과들이 있다.
## 4. 첫번째 수를 시작으로 수를 순차적으로 빼면 된다.

oper=input()
opers=oper.split('-')

result=[]
for oper in opers:
    o=sum(list(map(int, oper.split('+'))))
    result.append(o)

ans=result[0]
for i in range(1, len(result)):
    ans-=result[i]
print(ans)

