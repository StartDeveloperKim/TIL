pos=input()
aton={'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
px, py=int(pos[1])-1, aton[pos[0]]

dx=[-2, -1, 1, 2, 2, 1, -1, -2] # 상하
dy=[-1, -2, -2, -1, 1, 2, 2, 1] # 좌우

ans=0
for x, y in zip(dx, dy):
    nx=px+x
    ny=py+y
    if 0<=nx<8 and 0<=ny<8:
        ans+=1
print(ans)
