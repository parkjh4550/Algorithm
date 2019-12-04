# https://programmers.co.kr/learn/courses/30/lessons/42585?language=python3
def solution(arrangement):
    answer = 0
    stack = []
    for i in range(len(arrangement)-1):
        # 1. 레이저인지 확인.
        if arrangement[i] == '(' and arrangement[i+1] == ')':
            answer+=len(stack)
            continue

        # 2. 괄호 종류 확인
        if arrangement[i] == '(':
            answer+=1
            stack.append(arrangement[i])
        elif arrangement[i] == ')' and arrangement[i-1] != '(':
            stack.pop()

    return answer


print(solution('()(((()())(())()))(())'))