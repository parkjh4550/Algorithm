# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/49089/%EC%9D%B8%EC%8B%B8%EA%B0%80-%EB%90%98%EA%B3%A0-%EC%8B%B6%EC%9D%80-%EB%AF%BC%EC%88%98/quiz/1
# 해법 : 1이상 구간에서는 항상 "2"가 가장 많이 등장하는 약수
start, end = list(map(int, input().split()))
if start != end:
    print("2")
else:
    flag = False
    for num in range(2, int(start ** (1 / 2)) + 1):
        if start % num == 0:
            print(num)
            flag = True
            break

    if not flag:
        print(start)