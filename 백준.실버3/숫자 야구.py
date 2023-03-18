from itertools import permutations

n=int(input())
questions=[list(map(int, input().split())) for _ in range(n)]
nums=list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

for ques in questions:
    remove_cnt=0
    for i in range(len(nums)):
        strike, ball=0, 0
        i-=remove_cnt

        number=list(str(ques[0]))
        for j in range(3):
            if int(number[j]) == nums[i][j]:
                strike+=1
            elif int(number[j]) in nums[i]:
                ball+=1

        if ques[1]!=strike or ques[2]!=ball:
            nums.remove(nums[i])
            remove_cnt+=1
print(len(nums))

