## 첫번째 반복은 노락색 네모의 가로와 세로를 알기 위한 반복문이다.
## 가로가 세로보다 길다는 조건이 있으므로 int(yellow**0.5)+1까지 해도된다.
## 구해진 노란색의 가로와 세로 길이를 통해 그 때의 갈색타일의 개수를 계산한다.
## 이 때의 갈색타일의 개수가 파라미터로 전달된 갈색타일의 개수와 같다면 이때 전체 네모의 가로와 세로를 반환한다.

def solution(brown, yellow):
    for h in range(1, int(yellow**0.5)+1):
        if yellow%h==0:
            temp_brown=((yellow/h)*2+4)+(h*2)
            if temp_brown==brown:
                return [(yellow/h)+2, h+2]
