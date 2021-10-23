# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 문제 : https://level.goorm.io/exam/43275/%EC%99%84%EC%A0%84%EC%88%98/quiz/1
def get_divisor(number:int):
	list_divisor = []
	sqrt_number = int(number**(1/2))
	for div in range(1, sqrt_number+1):
		if number%div == 0:
			list_divisor.append(div)
			list_divisor.append(number//div)
	return list_divisor

def is_complete_number(number:int):
	list_divisor = get_divisor(number)
	if sum(list_divisor)-number == number:
		return True
	return False

user_input = input()
min_number, max_number = list(map(int, user_input.split()))

list_complete_number = []
for number in range(min_number, max_number+1):
	if number == 1: continue
	if is_complete_number(number):
		list_complete_number.append(number)
print(' '.join([str(num) for num in list_complete_number])+' ')
