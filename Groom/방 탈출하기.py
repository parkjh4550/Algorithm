# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/49105/%EB%B0%A9-%ED%83%88%EC%B6%9C%ED%95%98%EA%B8%B0/quiz/1
# 해법 : 퀵 정렬 + 이진 탐색
def binary_search(target: int, list_numbers: list):
    start = 0
    end = len(list_numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if list_numbers[mid] == target:
            return mid
        elif list_numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


num_numbers = int(input())
list_numbers = list(map(int, input().split()))
num_targets = int(input())
list_targets = list(map(int, input().split()))

list_numbers.sort()
for target in list_targets:
    is_element = binary_search(target, list_numbers)
    if is_element != None:
        print(1)
    else:
        print(0)