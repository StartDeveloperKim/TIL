def solution(k, tangerine):
    answer = 0
    tangerineDic={}
    for t in tangerine:
        if t in tangerineDic.keys(): tangerineDic[t]+=1
        else: tangerineDic[t]=1

    box=[]
    for key, v in tangerineDic.items():
        box.append([key, v])
    box.sort(key=lambda x:x[1], reverse=True)

    total=0
    for b in box:
        total+=b[1]
        answer+=1
        if total>=k:
            break
    return answer
