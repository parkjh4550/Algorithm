# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/49111/%EC%99%B8%EA%B3%84%EC%9D%B8%EA%B3%BC-%EC%9A%A9%EB%8F%88%EA%B8%B0%EC%9E%85%EC%9E%A5/quiz/1
# 참고 : https://edu.goorm.io/qna/5563
num_days, num_period = list(map(int, input().split()))
list_money = list(map(int, input().split()))
list_period = [list(map(int, input().split())) for _ in range(num_period)]
list_sum = [list_money[0]]
for itr in range(1, len(list_money)):
	list_sum.append(list_sum[itr-1]+list_money[itr])
#print(list_sum)
score = lambda sum_money: ("+" if sum_money > 0 else "") + str(sum_money)
for start, end in list_period:
	#입력이 길어질수록 sum 계산에 시간이 오래 걸린다
	#sum_money = sum(list_money[start-1:end])
	if start == 1:
		sum_money = list_sum[end-1]
	elif start == end:
		sum_money = list_money[end-1]
	else:
		sum_money = list_sum[end-1] - list_sum[start-1-1]
	print(score(sum_money))

