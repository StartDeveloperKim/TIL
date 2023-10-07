# 택배상자 크기 모두 같음 / 1번부터 n번까지 번호가 증가하는 순서대로 일렬로 놓임
# 택배 기사님이 알려준 순서 = order
# 보조 컨테이너 벨트 추가 설치, 맨 앞의 상자만 뺄 수 있음 = stack 구조로 동작
# 기사님이 원하는 순서대로 상자를 싣지 못한다면, 더 이상 상자를 싣지 않는다.

# main_belt = [4, 3]
# assis_belt = [1, 2, 3, 5] -> 그 다음 1을 넣어야 하는데 못 빼기 때문에 안됨 

# 두 번의 검사를 해야한다. main_belt와 assis_belt[-1]

from collections import deque

def solution(order):
    first_len=len(order)
    assis_belt=[]
    
    man_order=deque(order) # 아저씨 주문
    max_value=max(order)
    box=1
    while man_order:
        now_box = man_order[0]
        if now_box==box: # 메인 벨트의 1번이랑 주문 1번이랑 일치
            man_order.popleft()
        elif assis_belt and assis_belt[-1]==now_box: # 보조 1번이랑 주문 1번이랑 일치
            man_order.popleft()
            assis_belt.pop()
            continue
        else:
            assis_belt.append(box)
        
        if max_value<box: # 메인 벨트가 끝까지 돌았다면
            if assis_belt[-1]==now_box: 
                assis_belt.pop()
                man_order.popleft()
            elif assis_belt[-1]!=now_box:
                break
        
        box+=1 # 다음 박스
            
    return first_len-len(man_order)
