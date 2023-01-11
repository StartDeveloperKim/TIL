## 알고리즘
## 1. 헤더, 숫자, 테일 중 숫자를 구한다면 헤더와 테일을 구할 수 있다.
## 2. 숫자는 5글자 이하여야 한다.
## 3. head와 tail을 구할 때 maxsplit을 1로 한 것은 tail에 동일한
##    숫자가 나올 수 있기 때문이다. -> 이 처리를 안해서 런타임에러 발생
## 4. 정렬 기준은 헤더 소문자기준(대,소문자 구분X), 숫자 순서로 처리한다.
## 5. 다시 문자열로 묶어 반환한다.

def solution(files):
    filesDiv=[]
    for file in files:
        number=''
        for i in range(len(file)):
            if file[i].isdigit():
                number+=file[i]
            elif len(number)==0:
                continue
            else:
                break

            if len(number)==5:
                break
        head, tail = file.split(number, maxsplit=1)
        filesDiv.append([head, number, tail])
    filesDiv.sort(key=lambda x:(x[0].lower(), int(x[1]), ))

    return [''.join(file) for file in filesDiv]
