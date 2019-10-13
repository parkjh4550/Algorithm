def DFS(map, map_visit, start, region):
    # map : binary map
    # map_visit : already visited map by DFS
    # start : start point for DFS
    # region : number of check on the map_visit

    stack = list()
    stack.append(start)
    map_size = len(map)
    while stack:
        current_point = stack.pop()
        y, x = current_point[0], current_point[1]
        search_space = [[y+1,x], [y-1,x], [y,x+1], [y,x-1]]
        for p in search_space:
            if p[0] < map_size and p[0] >= 0 and p[1] < map_size and p[1] >= 0:
                if map[p[0]][p[1]] and (not map_visit[p[0]][p[1]]):
                    map_visit[p[0]][p[1]] = region
                    stack.append(p)
    return map, map_visit

map = [[0,1,1,0,1,0,0],
       [0,1,1,0,1,0,1],
       [1,1,1,0,1,0,1],
       [0,0,0,0,1,1,1],
       [0,1,0,0,0,0,0],
       [0,1,1,1,1,1,0],
       [0,1,1,1,0,0,0]]


if __name__ == '__main__':
    region = 1
    map_size = 7
    visit = [[0 for j in range(0, map_size)] for i in range(0, map_size)]
    for y in range(map_size):
        for x in range(map_size):
            if map[y][x] and (not visit[y][x]):
                map, visit = DFS(map=map, map_visit=visit, start=[y,x], region=region)
                region+=1
    for line in visit:
        print(line)