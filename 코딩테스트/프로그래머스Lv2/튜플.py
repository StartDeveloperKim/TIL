# 튜플 : 셀수있는 수량의 순서있는 열거 또는 어떤 순서를 따르는 요소들의 모음
# n개의 요소를 가진 튜플 : n-tuple
# 아래의 성질을 가지고 있음
#  중복 원소 o / 순서가 있음 / 개수는 유한

def solution(s):
    answer = []
    
    sets=[]
    temp=[]
    num=''
    for ch in s:
        if ch=='{': # start
            temp=[]
        elif ch==',' and len(num)>0: # 숫자종료
            temp.append(int(num))
            num=''
        elif ch=='}' and len(num)>0: # end
            temp.append(int(num))
            sets.append(temp)
            num=''
        elif ch.isdigit():
            num+=ch
    
    sets.sort(key=lambda x: len(x))
    
    for s in sets:
        for n in s:
            if n not in answer:
                answer.append(n)
                break
              
    return answer
