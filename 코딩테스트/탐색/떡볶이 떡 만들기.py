##손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에
##설정할 수 있는 높이의 최댓값을 구하는 프로그램

n, m=map(int, input().split())
data=list(map(int, input().split()))

start=0
end=max(data)

result=0
while start <= end:
    total = 0
    mid = (start+end)//2

    for x in data:
        if x>mid:
            total += x-mid
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)
