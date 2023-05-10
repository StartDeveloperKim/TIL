def sequentialSearch(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

# 문자열이 몇번째에 존재하는지 알 수 있다.
print(sequentialSearch(n, target, array)) 
