from collections import Counter

def solution(str1, str2):
    answer = 0

    s1, s2=[], []
    def divideList(sList, result):
        for i in range(len(sList)):
            temp = sList[i:i+2]
            if temp.isalpha() and len(temp)==2:
                result.append(temp.lower())

    divideList(str1, s1)
    divideList(str2, s2)

    multiset1, multiset2=Counter(s1), Counter(s2)

    intersectionSet=multiset1 & multiset2
    unionSet = multiset1 + multiset2

    intersection=sum(intersectionSet.values())
    union=sum(unionSet.values())-intersection

    if union==0 and intersection==0:
        return 65536

    return int((intersection/union)*65536)
