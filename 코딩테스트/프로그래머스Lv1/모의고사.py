## 완전탐색 문제
## answers의 길이만큼 one, two, three의 리스트를 늘려줬다.
## 그 후 정답과 비교를 통해 맞춘개수를 연산
## 최대로 맞춘 학생의 인덱스를 answer에 추가하여 반환

def solution(answers):
    result = [0, 0, 0]
    problem_cnt=len(answers)
    one=[1, 2, 3, 4, 5]*(problem_cnt//5+1)
    two=[2, 1, 2, 3, 2, 4, 2, 5]*(problem_cnt//8+1)
    three=[3, 3, 1,1, 2, 2, 4, 4, 5, 5]*(problem_cnt//10+1)
    
    for idx, stu in enumerate([one, two, three]):
        for i in range(problem_cnt):
            if stu[i]==answers[i]:
                result[idx]+=1
    
    max_cnt=max(result)
    answer=[i+1 for i in range(len(result)) if result[i]==max_cnt]
    
    return answer
