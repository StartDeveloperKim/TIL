# DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하자.
# cacheSize(0~30), cities(max, 100,000)
# 도시이름은 영문자로 이뤄져있음, 대소문자 구분x, 이름 최대 20자
# 캐시 교체 알고리즘은 LRU(최근 사용된 거)
# cache hit일 경우 실행시간 1 / miss일 경우 실행시간 5

# 1. 캐시 교체 알고리즘이 LRU이기 때문에 최근 사용된 것 
# 2. 캐시 사이즈에 꽉 차있지 않다면 cache에 데이터를 넣어야 한다.
#   하지만 이때 해당 도시가 있는지 없는지 확인해야 한다.
from collections import deque

def solution(cacheSize, cities):
    if cacheSize==0:
        return 5*len(cities)
    
    answer = 0
    cache=deque()
    for c in cities:
        city = c.lower()
        if len(cache)<cacheSize and city not in cache:
            cache.appendleft(city)
            answer+=5
            continue
            
        if city in cache: # cache hit
            cache.remove(city)
            cache.appendleft(city)
            answer+=1
        elif city not in cache: # cache miss
            cache.pop()
            cache.appendleft(city)
            answer+=5
    
    return answer
