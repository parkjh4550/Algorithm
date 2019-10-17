#https://programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    division = 1000000007

    # 맵형성 1: 이런식으로 map을 형성하면 모두 같은 주소값을 가져서 함께 변하게 된다.
    #path = [[0] * m] * n
    # 맵형성 2:
    path = []
    for itr in range(n):
        tmp = []
        for itr2 in range(m):
            tmp.append(0)
        path.append(tmp)
    #print(path)
    # find puddle


    min_x, min_y = m, n
    for pud in puddles:
        x, y = pud[0]-1, pud[1]-1
        if y == 0:
            if x < min_x: min_x = x
        elif x == 0:
            if y < min_y: min_y = y

    # initialize map
    for x in range(0, min_x):
        path[0][x] = 1
    for y in range(0, min_y):
        path[y][0] = 1

    for line in path:
        print(line)
    print(puddles)
    # clac path
    for y in range(1, n):
        for x in range(1, m):
            if [x + 1, y + 1] in puddles:
                print('in')
                path[y][x] = 0
            else:
                path[y][x] = path[y - 1][x] + path[y][x - 1]
            print(str(y) + ', ' + str(x) + ' : ' + str(path[y][x]))
        print(path)
    print('after calc')
    for line in path:
        print(line)
    answer = path[n - 1][m - 1] % division
    return answer


print(solution(5,	7,	[[2, 0], [1,4],[2,2],[4,4]]))