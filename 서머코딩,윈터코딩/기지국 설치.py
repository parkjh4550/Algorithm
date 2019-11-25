# https://programmers.co.kr/learn/courses/30/lessons/12979?language=python3

def solution(n, stations, w):
    answer = 0

    for index, s in enumerate(stations):
        if index==0:
            start = 1
            end = s-w
        else:
            start = stations[index-1] + w +1
            end = s-w

        length = end-start
        need = length//(2*w+1)
        if length%(2*w+1)>0: need +=1
        answer+= need

    if stations[-1]+w < n:
        start, end = stations[-1]+w+1, n
        length = end - start
        if length ==0: answer+=1
        else:
            need = length // (2 * w + 1)
            if length % (2 * w + 1) > 0: need += 1
            answer += need

    return answer


print(solution(11, [4,11], 1))
print(solution(16,[9],2))