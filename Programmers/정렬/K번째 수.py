#https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    array = list(map(int, array))
    for start, end, index in commands:
        tmp_a = array[start-1:end]
        tmp_a.sort()
        answer.append(tmp_a[index-1])
    return answer