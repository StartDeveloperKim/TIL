n, m=map(int, input().split())
numbers=[list(map(int, input().split())) for _ in range(n)]

result=[]
for i in range(n):
    result.append(min(numbers[i]))
print(max(result))
