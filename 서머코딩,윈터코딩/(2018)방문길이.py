# https://programmers.co.kr/learn/courses/30/lessons/49994?language=python3

def solution(dirs):
    answer = 0
    left_limit, right_limit = -5, 5
    top_limit, bottom_limit = 5, -5
    start = [0,0]
    visit = []
    reverse_visit=[]
    for command in dirs:
        if command == 'U':
            new_y = start[1]+1
            if new_y>top_limit:
                new_y = top_limit
            else:
                path = str(start[0])+str(start[1])+command
                if path not in reverse_visit:
                    visit.append(path)
                    reverse_visit.append(str(start[0])+str(new_y)+'D')
            start = [start[0], new_y]


        elif command =='D':
            new_y = start[1] - 1
            if new_y < bottom_limit:
                new_y = bottom_limit
            else:
                path = str(start[0])+str(start[1])+command
                if path not in reverse_visit:
                    visit.append(path)
                    reverse_visit.append(str(start[0])+str(new_y)+'U')
            start = [start[0], new_y]

        elif command =='R':
            new_x = start[0] + 1
            if new_x > right_limit:
                new_x = right_limit
            else:
                path = str(start[0])+str(start[1])+command
                if path not in reverse_visit:
                    visit.append(path)
                    reverse_visit.append(str(new_x)+str(start[1])+'L')
            start = [new_x, start[1]]

        elif command =='L':
            new_x = start[0] - 1
            if new_x < left_limit:
                new_x = left_limit
            else:
                path = str(start[0])+str(start[1])+command
                if path not in reverse_visit:
                    visit.append(path)
                    reverse_visit.append(str(new_x)+str(start[1])+'R')
            start = [new_x, start[1]]

    return len(set(visit)-set(reverse_visit))

print(solution("LULLLLLLU"))
print(solution("LR"))