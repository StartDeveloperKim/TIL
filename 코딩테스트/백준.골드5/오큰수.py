def solution(numbers):
    answer = []
    length=len(numbers)
    cache={}
    
    for i in range(length):
        if numbers[i] in cache.keys() and cache[numbers[i]][0]>i:
            answer.append(cache[numbers[i]][1])
        else:
            for j in range(i, length):
                if numbers[i]<numbers[j]:
                    cache[numbers[i]]=[j, numbers[j]] # value로 (인덱스, 값)
                    answer.append(numbers[j])
                    break
            else:
                answer.append(-1) 
                cache[numbers[i]]=[length, -1]
    return answer

n=int(input())
numbers=list(map(int, input().split()))

answer=solution(numbers)
for n in answer:
    print(n, end=' ')
