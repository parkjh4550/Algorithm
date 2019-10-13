#https://programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    # (sign, index, cal_num)
    stack = [(-1, 0, 0), (1, 0, 0)]
    max_len = len(numbers)-1

    while stack:
        current = stack.pop()
        cal_num = current[2] + numbers[current[1]] * current[0]
        if current[1] == max_len:
            if cal_num == target:
                answer+=1
            continue

        stack.append((-1, current[1] + 1, cal_num))
        stack.append((1, current[1] + 1, cal_num))

    return answer