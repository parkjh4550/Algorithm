# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/43232/%EC%95%BD%EC%88%98%EC%9D%98-%ED%95%A9/quiz/1
user_input = int(input())

sqrt_number = int(user_input**(1/2))
list_divisor = []
for div in range(1, sqrt_number+1):
	if user_input==1:
		list_divisor.append(1)
		break
	if user_input % div == 0:
		list_divisor.append(div)
		if div!=user_input//div:
			list_divisor.append(user_input//div)
print(sum(list_divisor))
"""
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i == 0:
            answer += i
    return answer

print(solution(user_input))
"""
