# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/43238/%EC%86%8C%EC%88%98-%ED%8C%90%EB%B3%84/quiz/1#
user_input = int(input())

answer = True
max_number=int(user_input**(1/2))
for i in range(2, max_number+1):
	left = user_input % i
	if left == 0:
		answer = False
		break
print(answer)
#print ("Hello Goorm! Your input is " + user_input)
