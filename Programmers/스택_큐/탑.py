# https://programmers.co.kr/learn/courses/30/lessons/42588

def solution(heights):
    answer = []
    if len(heights) <= 1: return [0]

    heights.reverse()
    flag = False
    for itr in range(len(heights) - 1):
        for itr2 in range(itr, len(heights)):
            if heights[itr] < heights[itr2]:
                flag = True
                answer.append(len(heights) - itr2)
                break
        if not flag: answer.append(0)
        flag = False
    answer.append(0)
    answer.reverse()

    return answer