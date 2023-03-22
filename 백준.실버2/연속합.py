import sys
input=sys.stdin.readline

n=int(input())
numbers=list(map(int, input().split()))

number_sum=[numbers[0]]
for i in range(n-1):
    number_sum.append(max(number_sum[i]+numbers[i+1] ,numbers[i+1]))

print(max(number_sum))
