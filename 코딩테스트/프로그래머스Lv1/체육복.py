def solution(n, lost, reserve):
    def remove_student_num(number):
        lost.remove(number)
    # 문제에 lost와 reserve가 오름차순으로 정렬되어 제공된다는 이야기가 없었기에 해줬다.
    lost.sort() 
    reserve.sort()
    
    temp_reserve=[] # 여벌을 가져왔지만 잃어버린 사람을 제외 
    for r_stu in reserve:
        if r_stu in lost:
            remove_student_num(r_stu)
        else:
            temp_reserve.append(r_stu)
    
    for r_stu in temp_reserve:
        if r_stu-1 in lost:
            remove_student_num(r_stu-1)
        elif r_stu+1 in lost:
            remove_student_num(r_stu+1)
    return n-len(lost)
