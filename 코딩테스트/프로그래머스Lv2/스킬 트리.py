##주어진 스킬트리에서 체크해야할 스킬만 추출한다.
##스킬은 처음부터 배워야하므로 주어진 skill의 순서와 추출된 skill_tree의 순서를 서로 비교한다.

def check_skill_tree(skill_tree, skill):
    if ''.join(skill[:len(skill_tree)])==skill_tree:
        return True
    return False
            

def solution(skill, skill_trees):
    answer = 0
    skill_set=list(skill)
    for skills in skill_trees:
        skill_tree=""
        for skill in list(skills):
            if skill in skill_set:
                skill_tree+=skill

        if check_skill_tree(skill_tree, skill_set):
            answer+=1
            
    return answer
