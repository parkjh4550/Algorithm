# https://programmers.co.kr/learn/courses/30/lessons/49191?language=python3

def solution(n, results):
    answer = 0
    win, lose = {}, {}
    for i in range(1, n+1):
        win[i] = set()
        lose[i] = set()

    results.sort()
    for i in range(1,n+1):
        for re in results:
            if re[0]==i:
                win[i].add(re[1])
            if re[1]==i:
                lose[i].add(re[0])

        for j in win[i]:
            lose[j].update(lose[i])
        for j in lose[i]:
            win[j].update(win[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer+=1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))