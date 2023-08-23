# 날짜계산을 위한 모듈 datetime
# -> 마이크로초, 밀리초, 초, 분, 시간, 일, 주를 원하는 만큼 더하고 뺀다.
# 동일하게 날짜 계산을 위한 모듈 dateutil.relativedelta
# -> datetime과 거의 비슷하지만 월, 년을 원하는 만큼 더하고 뺄 수 있다.

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    termDict = {}

    t=list(map(int, today.split('.')))
    todayDate = datetime(t[0], t[1], t[2])
    for term in terms:
        discriminant = term.split(' ')
        termDict[discriminant[0]] = discriminant[1]

    def calculatorDate(month, date):
        d=list(map(int, date.split('.')))
        start = datetime(d[0], d[1], d[2])
        end = start + relativedelta(months=int(month)) - relativedelta(days=1)

        return True if ((todayDate-end).days) > 0 else False

    for i, privacy in enumerate(privacies):
        p = privacy.split(' ')
        result=calculatorDate(termDict[p[1]], p[0])
        if result:
            answer.append(i+1)
    return answer
