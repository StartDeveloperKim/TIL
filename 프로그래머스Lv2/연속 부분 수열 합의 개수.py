def solution(elements):
    answer = set()
    elements=elements+elements
    for i in range(1, len(elements)//2+1):
        start=0
        for j in range(len(elements)//2):
            answer.add(sum(elements[start:start+i]))
            start+=1
    return len(answer)
