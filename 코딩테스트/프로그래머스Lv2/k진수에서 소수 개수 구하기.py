def isPrime(num):
    if num==1:
        return False
    if num==2:
        return True
    for n in range(2, int(num**0.5)+1):
        if num%n==0:
            return False
    return True

def solution(n, k):
    answer = 0
    kBinary=[]

    while n!=0:
        kBinary.append(str(n%k))
        n//=k

    kBinary.reverse()
    check=''.join(kBinary).split('0')

    for n in check:
        if n!='':
            if isPrime(int(n)):
                answer+=1

    return answer
