## 알고리즘
## 1. stack의 마지막 인덱스 숫자가 입력된 숫자가 같지않다면
##    같을 때까지 숫자 리스트에서 pop을 진행하고 append한다.
##    이 때 정답 리스트에 +를 넣는다.
## 2. stack의 마지막 숫자가 입력된 숫자와 같다면 pop을 진행하고 정답리스트에 -를 넣는다.
## 3. n번 반복한다.
## 4. stack의 원소가 남아있다는 것은 수열을 만들지 못한다는 의미이므로 NO를 출력한다.

n=int(input())
num=[i for i in range(n, 0, -1)]
stack, ans=[], []

for _ in range(n):
    number=int(input())
    if len(stack)==0 or stack[-1]!=number:
        while len(num)!=0:
            stack.append(num.pop())
            ans.append('+')
            if stack[-1]==number:
                break
    if stack[-1]==number:
        stack.pop()
        ans.append('-')

if len(stack)==0:
    for a in ans:
        print(a)
else:
    print('NO')
