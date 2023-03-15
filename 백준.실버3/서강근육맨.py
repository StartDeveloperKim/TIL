n=int(input())
lost=list(map(int, input().split()))

def solution(start, end, lost, min_lost):
    
    while start<end:
        print(start, end, lost, min_lost)
        temp=lost[start]+lost[end]
        if temp > min_lost:
            min_lost=temp
        start+=1
        end-=1
        
    return min_lost

lost.sort()
start, end = 0, n-1
result=-1
if n%2:
    min_lost=lost[end]
    end-=1
    result=solution(start, end, lost, min_lost)
else:
    result=solution(start, end, lost, -1)
print(result)
