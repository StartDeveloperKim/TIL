import heapq
heap=[]
# 파이썬의 heapq는 최소힙으로 작동한다.

def heap_sort():
    # heap에서 숫자를 pop할때는 작은값부터 뽑기에 뽑아서 append한다면 정렬이된다.
    sorted_num=[]
    while heap:
        sorted_num.append(heapq.heappop(heap))
    return sorted_num

def kth_smallest(k):
    # k번 수를 pop()하면 k번째 작은 값을 구할 수 있다.
    minNum=None
    for _ in range(k):
        minNum=heapq.heappop(heap)
    return minNum

# 힙에 원소 추가 -> heappush(리스트, 추가할 원소)
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

# 힙 원소 삭제 -> heappop(리스트)
for _ in range(4):
    # 작은 값부터 pop()이된다.
    print(heapq.heappop(heap))
