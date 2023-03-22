n, s=map(int, input().split())
numbers=list(map(int, input().split()))
ans=0
num=[]
    
def solution(idx):
    global ans
    if sum(num)==s and len(num)>0:
        ans+=1

    for i in range(idx, n):
        num.append(numbers[i])
        print(num)
        solution(i+1)
        num.pop()
        print(num)

solution(0)
print(ans)
    
