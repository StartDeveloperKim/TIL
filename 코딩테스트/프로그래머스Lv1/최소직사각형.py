## 완전탐색 문제였다.
## 최소직사각형을 많들기 위해서는 높이와 폭 중 하나는 최솟값 하나는 최대값이여야한다.
## 따라서 반복문을 통해 회전을 하는 작업을 했다.

def solution(sizes):
    answer=[[], []]
    for size in sizes:
        answer[0].append(min(size))
        answer[1].append(max(size))
    return max(answer[0])*max(answer[1])
