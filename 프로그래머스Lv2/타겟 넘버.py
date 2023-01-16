## 알고리즘
## 1. 가능한 모든 수식을 시도한다.(DFS를 통한 완전탐색)
## 2. 처음 수부터 +, - 각각의 연산자부터 시작한다.

answer = 0
def solution(numbers, target):
    
    def dfs(idx, value):
        global answer
        if idx==len(numbers) and target==value:
            answer+=1
            return
        
        if idx==len(numbers):
            return
        dfs(idx+1, value+numbers[idx])
        dfs(idx+1, value-numbers[idx])
    
    dfs(0, 0)
    return answer
