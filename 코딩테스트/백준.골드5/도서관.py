n, m=map(int, input().split())
position=list(map(int, input().split()))
posit, negat=[], []

for p in position:
    if p>0:
        posit.append(p)
    else:
        negat.append(abs(p))

posit.sort(reverse=True)
negat.sort(reverse=True)
distance=[]

for i in range(len(posit)//m):
    distance.append(posit[m*i])
if len(posit)%m>0:
    distance.append(posit[(len(posit)//m)*m])

for i in range(len(negat)//m):
    distance.append(negat[m*i])
if len(negat)%m>0:
    distance.append(negat[(len(negat)//m)*m])

distance.sort()
result=distance.pop()
result+=2*sum(distance)
print(result)
