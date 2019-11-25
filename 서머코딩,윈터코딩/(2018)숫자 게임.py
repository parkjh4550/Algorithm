# https://programmers.co.kr/learn/courses/30/lessons/12987?language=python3

def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    check = [False for _ in range(len(B))]
    last = 0
    for elem in A:
        #  이전 차례 때 선발됬던 B이후로 뽑는것이 효율적, 어차피 그 앞에 얘들은 못 뽑힘.
        for itr in range(last, len(B)):
            elem2 = B[itr]
            if elem<elem2 and check[itr] == False:
                answer+=1
                check[itr] = True
                last=itr
                break


    return answer


print(solution([5,1,3,7], [2,2,6,8]	))