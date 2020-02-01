#https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3

def solution(progresses, speeds):
    answer = []
    result = {}
    full_work = 100
    last_distribute = 0

    for work, progress in enumerate(progresses):
        remain = full_work - progress

        distribute = remain // speeds[work]
        if remain % speeds[work]: distribute += 1
        if distribute < last_distribute:
            distribute = last_distribute
        else:
            last_distribute = distribute
        if distribute in result:
            result[distribute] += 1
        else:
            result[distribute] = 1

    distribute = sorted(list(result.keys()))
    print(distribute)
    for d in distribute:
        answer.append(result[d])

    return answer