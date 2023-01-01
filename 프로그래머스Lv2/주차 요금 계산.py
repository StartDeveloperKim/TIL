from math import ceil

def calculateTime(inTime, outTime):
    time1=inTime.split(':')
    time2=outTime.split(':')
    start = int(time1[0])*60+int(time1[1])
    end = int(time2[0])*60+int(time2[1])

    return end-start

def calculateFee(time, fees):
    accumulate = (time-fees[0]) if (time-fees[0])>0 else 0 
    return fees[1] + ceil(accumulate/fees[2])*fees[3]

def solution(fees, records):
    answer = []
    carDic, timeDic={}, {}

    for record in records:
        car = record.split(' ')
        if car[1] not in carDic.keys():
            carDic[car[1]]=[car[0], car[2]]
            timeDic[car[1]]=0
        else:
            #요금 계산
            if car[2]=='OUT':
                time = calculateTime(carDic[car[1]][0], car[0])
                timeDic[car[1]]+=time
            # 입출 시간, 입출여부 변환
            carDic[car[1]]=[car[0], car[2]]

    # 출차안된차 출차
    for k, v in carDic.items():
        if v[1]=='IN':
            time = calculateTime(v[0], '23:59')
            timeDic[k]+=time

    for k, v in timeDic.items():
        answer.append([k, calculateFee(v, fees)])

    answer.sort(key=lambda x:x[0])
    return [ans[1] for ans in answer]
