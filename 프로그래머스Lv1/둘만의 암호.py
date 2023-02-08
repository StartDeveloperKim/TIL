## 문제풀이:
##     1. skipAlpha를 set으로 둔다. 이는 in 연산에 대한 시간복잡도를 줄이기 위한 작업이다.
##     2. 반복문을 돌며 각각의 문자를 아스키코드로 변경한다.
##     3. 1씩 더해가며 해당 문자가 skipAlpha에 있는지 확인한다.
     
def solution(s, skip, index):
    answer = ''
    skipAlpha=set(skip)
    for ch in s:
        cnt=0
        asciiCh=ord(ch)
        while cnt!=index:
            asciiCh=asciiCh+1
            if asciiCh > 122:
                asciiCh=97
            if chr(asciiCh) in skipAlpha:
                continue
            else:
                cnt+=1
        answer+=chr(asciiCh)
    return answer
