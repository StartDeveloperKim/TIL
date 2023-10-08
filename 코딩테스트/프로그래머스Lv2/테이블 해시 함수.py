# 테이블은 2차원 행렬로 표현
# 열 = 컬럼 / 행 = 튜플
# 1C = PK 
# 1) 테이블의 튜플을 col번째 컬럼의 값을 기준으로 오름차순 정렬
# 2) 동일하면 기본키인 첫 번째 컬럼의 값을 기준으로 내림차순
# 3) S_i = (C1%i) + ... 
# 4) row_begin <= S_i <= row_end XOR 한 값을 해시 값으로 반환

def get_S_i(num_tuple, i):
    result=0
    for num in num_tuple:
        result+=(num%i)
    return result

def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:(x[col-1], -x[0]))

    for i in range(row_begin, row_end+1):
        answer=answer ^ get_S_i(data[i-1], i)

    return answer
