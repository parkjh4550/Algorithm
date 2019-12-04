# https://programmers.co.kr/learn/courses/30/lessons/42627?language=python3
"""
def solution(jobs):
    answer = 0
    # 1. 시작 지점을 기준으로 정렬
    jobs.sort(key=lambda x: x[0])

    # 2. 각 시작 바탕으로 ongoing task가 있는지 확인.
    #done = [False]*len(jobs)
    stack = [[ jobs[0][0], jobs[0][1], jobs[0][1]-jobs[0][0] ]]
    jobs = jobs[1:]
    start = 0
    while stack:
        stack = sorted(stack, key=lambda x:x[2])
        current = stack.pop(0)  # 가장 빨리 끝낼 수 있는 것을 선택.
        answer += ((start+current[2]) - current[0])

        for itr, job in enumerate(jobs):
            if job[0] >= start and job[0] <= start+current[2]:
                stack.append([job[0],job[1], job[1]-job[0]])
                jobs.pop(itr)

        start = start + current[2]

    return answer
"""


def solution(jobs):
    answer = 0
    # 1. 시작 지점을 기준으로 정렬
    #jobs = [ [i[1][0], i[1][1], i[0]] for i in sorted(enumerate(jobs), key=lambda x: x[1][0])]  #(start, end, index)
    jobs.sort(key=lambda x:(x[0],x[1]))     #먼저 시작하는 얘들이 우선
    jobs = [ [job[0], job[1], itr] for itr, job in enumerate(jobs)]
    # 2. 각 시작 바탕으로 ongoing task가 있는지 확인.
    done = [False]*len(jobs)
    done[0] = True
    stack = [[ jobs[0][0], jobs[0][1], jobs[0][2] ]]

    start = 0
    while stack:
        stack = sorted(stack, key=lambda x:(x[1],x[0]))     # 가장 빨리 처리할 수 있는것이 우선.
        current = stack.pop(0)  # 가장 빨리 끝낼 수 있는 것을 선택.
        #answer += ((start+current[1]-current[0]) - current[0])
        answer += ((start-current[0]) + (current[1]))

        prev_stack = len(stack)
        for itr, job in enumerate(jobs):
            if job[0] >= start and job[0] <= start+current[1] and not done[job[2]]:
                stack.append([job[0],job[1], job[2]])
                done[job[2]] = True
            start = start + current[1]

        if len(stack) == prev_stack:
            try:
                next = done.index(False)
                stack.append([job for job in jobs if job[2] == next][0])
                done[stack[-1][2]] = True
                start = stack[-1][0]
                continue
            except: pass


    return int(answer/len(jobs))

#print(solution([[1, 9], [0, 3], [2, 6]]))

#print(solution([[4, 5], [0, 3], [10, 4]]))

#print(solution([[1, 9], [1, 4], [1, 5], [1, 7], [1, 3]]))

#print(solution([[1, 9], [1, 4], [1, 5], [2, 7], [2, 3]]))

#print(solution([[0, 5], [1, 2], [5, 5]]))

#print(solution([[0, 3], [1, 9], [500, 6]]))