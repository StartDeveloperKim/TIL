# - 피로도 시스템
# - 최소 필요 피로도 : 탐험을 시작하기 위해 필요함
# - 소모 피로도 : 탐험을 마쳤을 때 소모됨
# - 유저가 던전들을 최대한 많이 탐험하려 한다.
# - [최소필요 피로도, 소모 피로도] = dungeons

순열을 활용하여 가능한 모든 경우를 구한 후 완전탐색을 돌린다.
이 것이 가능한 이유는 던전의 개수가 최대 8개이기 떄문이다.
그리고 최대 던전개수를 구해야하기에 dungeons의 길이부터해서 거꾸로 순회한다.
  
from itertools import permutations

def solution(k, dungeons):
    for num in range(len(dungeons), 0, -1):
        for dungeon_list in permutations(dungeons, num):
            temp=k
            for dungeon in dungeon_list:
                if dungeon[0]<=temp:
                    temp-=dungeon[1]
                else:
                    break
            else:
                return num  
    return 0
