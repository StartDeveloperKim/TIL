def solution(players, callings):
    answer = []
    ranking1={value: idx for idx, value in enumerate(players)}
    ranking2={idx: value for idx, value in enumerate(players)}
    for calling in callings:
        name=ranking2[ranking1[calling]-1] # 현재 불린 선수의 바로 윗 순위 선수의 이름
        
        # 순위 최신화
        ranking1[calling]-=1
        ranking1[name]+=1
        
        # 순위별 선수 이름 최신화
        ranking2[ranking1[name]]=name
        ranking2[ranking1[calling]]=calling
    
    # 순위 오름차순으로 정렬
    sorted_dict=dict(sorted(ranking1.items(), key=lambda x:x[1]))

    return list(sorted_dict.keys())
