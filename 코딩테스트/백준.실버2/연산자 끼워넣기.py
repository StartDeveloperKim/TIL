## 알고리즘
## 1. result는 총 연산값으로 nums[0]부터 시작한다.
## 2. 각 연산자의 수를 하나씩 줄여가며 연산을 한다.
## 3. idx가 n과 같아졌을 경우는 마지막 수에 도달했는 것이므로
##    최대값과 최소값을 구한다.

from itertools import permutations

n=int(input())
nums=list(map(int, input().split()))
opers=list(map(int, input().split())) # +, -, *, //

maxAns, minAns = -1e10, 1e10

def calculator(nums, idx, result, opers):
    global maxAns, minAns
    if idx==n:
        maxAns=max(maxAns, result)
        minAns=min(minAns, result)
        return

    if opers[0]>0:
        opers[0]-=1
        calculator(nums, idx+1, result+nums[idx], opers)
        opers[0]+=1
    if opers[1]>0:
        opers[1]-=1
        calculator(nums, idx+1, result-nums[idx], opers)
        opers[1]+=1
    if opers[2]>0:
        opers[2]-=1
        calculator(nums, idx+1, result*nums[idx], opers)
        opers[2]+=1
    if opers[3]>0:
        opers[3]-=1
        calculator(nums, idx+1, int(result/nums[idx]), opers)
        opers[3]+=1


calculator(nums, 1, nums[0], opers)
print(maxAns)
print(minAns)
