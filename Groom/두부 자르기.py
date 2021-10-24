# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/49106/%EB%91%90%EB%B6%80-%EC%9E%90%EB%A5%B4%EA%B8%B0/quiz/1

# 1 1 1 1 1 1 1 -> 7  (첫 두부가 가장 크지 않기 때문에 count하지 않음)
#   2 1 1 1 1 1 -> 5  (1~5-썰기 수행 가능)
#     3 1 1 1 1 -> 4
#       4 1 1 1 -> 3
#         5 1 1 -> 2
#           6 1 -> 1

user_input = int(input())
cnt = 0
for i in range(user_input-2, 1, -1):
	cnt+=1
print(cnt)
