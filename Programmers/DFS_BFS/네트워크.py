#https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3
import copy


def solution(n, computers):
    answer = 0

    used = [[com, itr] for itr, com in enumerate(computers)]
    while used:
        stack = [used.pop(0)]
        path = [stack[0][1]]
        while stack:
            current = stack.pop()
            for itr, conn in enumerate(current[0]):
                if conn and itr != current[1] and itr not in path:
                    path.append(itr)
                    stack.append([computers[itr],itr])
        used = [ u for u in used if u[1] not in path]
        answer += 1

    return answer

print(solution(3,[[1,1,0],[1,1,0],[0,0,1]]))