from collections import deque

def solution(n, m, section):
    answer = 0
    section=deque(section)
    while section:
        start, end=section[0], section[0]+m
        while section:
            if start<=section[0]<=end-1:
                section.popleft()
            else:
                break
        answer+=1
        
    return answer
