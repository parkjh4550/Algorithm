#https://programmers.co.kr/learn/courses/30/lessons/12914?language=python3

# 피보나치 수열
def solution(n):
    answer = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2

    number = n // 2
    prev = 1
    current = 2
    for itr in range(3,n + 1):
        tmp = current
        current = current + prev
        prev = tmp
    return current%1234567

# 틀린 코드 , BFS로 해결하려 했음

# 각 경우 수를 factorial로 구하려 했음. 잘 안됨.
"""
from itertools import combinations
from itertools import permutations
from math import factorial


def solution(n):
    answer = 0
    if n == 1:
        return 1
    elif n == 2:
        return 2

    number = n // 2
    for itr in range(number + 1):
        num_elem = n - 2 * itr

        answer += int(factorial(n - itr) / (factorial(num_elem) * factorial(itr)))

        # case = [1] * num_elem + [2] *itr
        # print(set(list(permutations(case, len(case)))))
        # answer+=len(set(list(permutations(case, len(case)))))
    return answer%1234567
"""