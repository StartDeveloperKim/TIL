def solution(record):
    answer = []
    enterMsg="님이 들어왔습니다."
    leaveMsg="님이 나갔습니다."
    chatRoom={}

    for i in range(len(record)):
        info=record[i].split(" ")
        msg=info[0]
        if msg=="Enter":
            userId, nickname=info[1], info[2]
            if userId not in chatRoom.keys():
                chatRoom[userId]=[nickname, [i, msg]]
            else:
                if nickname!=chatRoom[userId][0]:
                    chatRoom[userId][0]=nickname
                chatRoom[userId].append([i, msg])
        elif msg=="Leave":
            chatRoom[info[1]].append([i, msg])
        else:
            chatRoom[info[1]][0]=info[2]

    for v in chatRoom.values():
        nickname=v[0]
        for i in range(1, len(v)):
            if v[i][1]=="Enter":
                answer.append([v[i][0], nickname+enterMsg])
            else:
                answer.append([v[i][0], nickname+leaveMsg])

    answer.sort(key=lambda x:x[0])
    return [m[1] for m in answer]
