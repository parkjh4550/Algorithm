# https://www.welcomekakao.com/learn/courses/30/lessons/43165
"""
# BFS Solution
def solution(numbers, target):
    answer = 0

    # (sign, index, cal_num)
    queue = [(-1, 0, 0), (1, 0, 0)]
    max_len = len(numbers)

    while queue:
        current = queue.pop(0)
        cal_num = current[2] + numbers[current[1]] * current[0]
        if current[1]+1 != max_len:
            queue.append((-1, current[1] + 1, cal_num))
            queue.append((1, current[1] + 1, cal_num))
        else:
            if cal_num == target: answer += 1
    return answer

print(solution([1,1,1,1,1], 3))
"""

# DFS solution
# This code successfully runned.
# I think 'pop(0)' on BFS function takes so much time
def solution(numbers, target):
    answer = 0

    # (sign, index, cal_num)
    stack = [(-1, 0, 0), (1, 0, 0)]
    max_len = len(numbers)-1

    while stack:
        current = stack.pop(0)
        cal_num = current[2] + numbers[current[1]] * current[0]
        if current[1] == max_len:
            if cal_num == target:
                answer+=1
            continue

        stack.append((-1, current[1] + 1, cal_num))
        stack.append((1, current[1] + 1, cal_num))

    return answer

print(solution([1,1,1,1,1], 3))


# beautiful code
# other person code
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])