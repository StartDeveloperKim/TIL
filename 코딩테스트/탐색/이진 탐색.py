def binarySearch(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2 # 중간점을 구한다.

    if array[mid]==target:
        return mid
    elif array[mid] > target: # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        return binarySearch(array, target, start, mid - 1)
    else: # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확
        return binarySearch(array, target, mid + 1, end)
