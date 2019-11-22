#https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

def solution(begin, target, words):
    answer = 0

    stack = [[begin, 0, 0, []]]
    used, result = [begin], []
    if target not in words: return 0    # target 단어가 없는 경우는 아예 빠져나간다.
    while stack:
        current = stack.pop()
        for itr, w in enumerate(words):
            if w in current[3]: continue
            if w in used: continue
            """
            tmp = set(list(w) + list(current[0]))
            # input = htt, output = hht  인 경우 제대로 비교를 하지 못한다.
            ## set을 안하면 w = hht 일 경우 tmp가 더 작아질 염려가 생긴다.
            if len(tmp) == len(set(w)) + 1:     
            """
            tmp = [c for i, c in enumerate(w) if c==list(current[0])[i]]
            if len(tmp) +1 == len(list(current[0])):

                # 어렵게 문자 변환할 필요가 없다.
                #new_word = str(list(set(list(w)) & set(list(current[0]))))
                #new_alpha = [alpha for alpha in list(w) if alpha not in new_word]
                #word1 = ''.join([alpha if alpha in new_word else new_alpha[0] for alpha in list(w)])
                #word1 = ''.join([alpha if alpha in new_word else new_alpha[0] for alpha in list(current[0])])
                word1 = w
                stack.append([word1, itr, current[2]+1, current[3]+[current[0]]])
                used.append(w)

                if word1 == target:result.append(stack[-1][2])
    return min(result)


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))