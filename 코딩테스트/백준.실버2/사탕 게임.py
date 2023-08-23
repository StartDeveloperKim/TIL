n=int(input())
candy=[list(input()) for _ in range(n)]
ans=1

def check(check_str):
    global ans
    global n
    alpha=['C', 'P', 'Z', 'Y']

    for a in alpha:
        for num in range(1, n+1):
            if num>ans and a*num in check_str:
                ans=max(num, ans)

def solution(candy, px, py, n):
    dx=[1, 0]
    dy=[0, 1]

    for x, y in zip(dx, dy):
        nx=px+x
        ny=py+y
        if 0<=nx<n and 0<=ny<n and candy[px][py]!=candy[nx][ny]:
            candy[px][py], candy[nx][ny]=candy[nx][ny], candy[px][py]
            for i in range(n):
                check(''.join(candy[i]))
                check(''.join(c[i] for c in candy))
            candy[px][py], candy[nx][ny]=candy[nx][ny], candy[px][py]

for i in range(n):
    check(''.join(candy[i]))
    check(''.join([c[i] for c in candy]))

for i in range(n):
    for j in range(n):
        solution(candy, i, j, n)
print(ans)
