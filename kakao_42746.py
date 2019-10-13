#https://www.welcomekakao.com/learn/courses/30/lessons/42746
def quicksort_sub(data, start, end):
    if end-start<=0:
        return

    pivot = data[end]
    i = start
    for j in range(start, end):
        if data[j]<= pivot:
            data[i], data[j]  = data[j], data[i]
            i+=1
    data[i], data[end] = data[end], data[i]

    #recursive
    quicksort_sub(data, start, i-1)
    quicksort_sub(data, i+1, end)
def quick_sort(data):
    quicksort_sub(data, 0, len(data)-1)

def compare(a, b):
    print(a+b, b+a)
    if int(a+b) >= int(b+a):
        return True
    return False
"""
def solution(numbers):
    answer = ''
    print(numbers)
    while True:
        flag = True
        for i in range(len(numbers)-1):
            if not compare(numbers[i], numbers[i+1]):
                tmp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = tmp
                flag = False
        if flag: break
    return ''.join(numbers)
"""
"""
def solution(numbers):
    if set(numbers) == set([0]): return '0'

    def compare(a, b):
        if int(a + b) >= int(b + a):
            return True
        return False

    # 미리 sorting  시켜서 빠르게 찾아줄려고 했음.
    # 하지만 통과 되었던 것에 한해서만 빨라짐.
    numbers = sorted(numbers, key=lambda x: str(x)[0], reverse=True)
    numbers = list(map(str, numbers))
    while True:
        flag = True

        for i in range(len(numbers) - 1):
            if not compare(numbers[i], numbers[i + 1]):
                tmp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = tmp
                flag = False
        if flag: break
    return ''.join(numbers)
"""

def solution(numbers):
    if set(numbers) == set([0]): return '0'

    def compare(a, b):
        if int(a + b) >= int(b + a):
            return True
        return False

    numbers = sorted(numbers, key=lambda x: str(x)[0], reverse=True)
    print(numbers)
    numbers = list(map(str, numbers))
    #앞자리 숫자 순대로 나열이 되므로, 앞자리 숫자가 같은 얘들끼리 비교해주려고 했었음.
    #하지만 여전히 실패.
    for itr in reversed(range(1,10)):
        while True:
            flag= True
            for i in range(len(numbers) - 1):
                if numbers[i][0]== str(itr) and numbers[i+1][0]==str(itr):
                    if not compare(numbers[i], numbers[i + 1]):
                        tmp = numbers[i]
                        numbers[i] = numbers[i + 1]
                        numbers[i + 1] = tmp
                        flag = False
            if flag: break
    return ''.join(numbers)

    numbers = list(map(str, numbers))
    while True:
        flag = True

        for i in range(len(numbers) - 1):
            if not compare(numbers[i], numbers[i + 1]):
                tmp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = tmp
                flag = False
        if flag: break
    return ''.join(numbers)



numbers = [3,30,34,5,9]
result = solution(numbers)
print(result)

numbers =[0,0]
if set(numbers) == set([0]): print('end')