def solution(want, number, discount):
    answer = 0
    for idx in range(len(discount)-9):
        discountProducts=discount[idx:idx+10]
        for w, n in zip(want, number):
            if discountProducts.count(w) < n:
                break
        else:
            answer+=1
    return answer
