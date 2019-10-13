def solution(N, number):
    # 1. Dynamic Programming

    answer = 0
    Gen = {1: [N]}
    answer += 1
    while answer < 8:
        tmp = []
        answer += 1
        for i in range(1, answer):
            j = (answer) - i
            for x in Gen[i]:
                for y in Gen[j]:
                    tmp.append(x + y)
                    tmp.append(x - y)
                    tmp.append(x * y)
                    if y > 0:
                        tmp.append(x // y)
                    elif y ==0 :
                        tmp.append(0)
                    #if list(set(x)):
                        #tmp.append(int(str(x) + str(y)))
            tmp.append(int(str(N)*answer))
        tmp = list(set(tmp))
        # print(tmp)
        #print(Gen)
        if number in tmp:
            return answer

        Gen[answer] = tmp

    return -1

    """
    # 2. DFS
    answer = 0
    # [Number, iteration]
    stack = [[N,1]]
    while stack:
        current = stack.pop()
        stack.append([current+N, 2])
        stack.append([current+N, 2])
        stack.append([current+N, 2])
        stack.append([current+N, 2])
        

    return -1
    """


examples  = [[5,12,4], [2,11,3]]

for sample in examples:
    result = solution(sample[0], sample[1])

    print('input : ', sample[:2])
    if result == sample[2]:
        print('correct')
    else:
        print('wrong')