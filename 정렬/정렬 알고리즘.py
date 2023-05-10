
def selectSort(array):

    for i in range(len(array)):
        min_index = 1
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_indx], array[i]

    return array

def insertSort(array):

    for i in range(len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array

def countSort(array):
    count = [0] * (max(array)+1)

    for i in range(len(array)):
        count[array[i]] += 1 #각 데이터에 해당하는 인덱스의 값 증가
    return count

    
