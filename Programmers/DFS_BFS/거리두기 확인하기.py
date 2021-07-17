# https://programmers.co.kr/learn/courses/30/lessons/81302
def check_partition(place, loc_p, delta_x, delta_y):
    if abs(delta_x) == 2:
        return place[loc_p[0]+delta_x-1][loc_p[1]] == 'X'
    if abs(delta_y) == 2:
        print(place)
        print(loc_p)
        print([loc_p[1]+delta_y-1])
        print(place[loc_p[0]][loc_p[1]+delta_y-1])
        return place[loc_p[0]][loc_p[1]+delta_y-1] == 'X'
    else:
        return place[loc_p[0]+delta_x][loc_p[1]] == 'X' and place[loc_p[0]][loc_p[1]+delta_y] == 'X'

def check_place(place):
    # 1. 모든 인물 위치 찾기
    loc_persons = []
    for x, row in enumerate(place):
        for y, col in enumerate(row):
            if col == 'P':
                loc_persons.append([x,y])
    # 2. 인물 선택
    for idx_p1, loc_p1 in enumerate(loc_persons):
        for loc_p2 in loc_persons[idx_p1+1:]:
            print(loc_p2, loc_p1)
            delta_x = loc_p2[0] - loc_p1[0]
            delta_y = loc_p2[1] - loc_p1[1]
            dist = abs(delta_x) + abs(delta_y)
            if dist==1:
                print('dist 1')
                return 0
            if dist==2:
                flag_partition = check_partition(place, loc_p1, delta_x, delta_y)
                print(flag_partition)
                if not flag_partition:
                    print('dist 2')
                    return 0
    print('success')
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(check_place(place))
    print(answer)
    return answer

if __name__ == '__main__':
    solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])