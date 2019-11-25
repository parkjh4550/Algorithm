
def solution(words, queries):
    answer = []

    for q in queries:
        len_q = len(q)
        if q[0]=='?':
            # ? : left side
            inv_q = q[::-1]
            left = len_q-inv_q.index('?')
            right = len_q

        else:
            # ? : right side
            left = 0
            right = q.index('?')

        answer.append(0)
        for w in words:
            if len(w) != len_q: continue
            flag= False
            for itr in range(left,right):
                if w[itr]!=q[itr]:
                    flag=True
                    break
            if not flag:
                answer[-1]+=1

            #if w[left:right] == q[left:right]:
                #answer[-1]+=1


    return answer


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))