n=int(input())
n_data=list(map(int, input().split()))
m=int(input())
m_data=list(map(int, input().split()))

answer=[]

def binarySearch(array, target, start, end):
    while start <= end:
        mid = (start+end)//2

        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

n_data.sort()

for i in m_data:
    if binarySearch(n_data, i, 0, len(n_data)-1)!=None:
        answer.append("yes")
    else:
        answer.append('no')

print(answer)
