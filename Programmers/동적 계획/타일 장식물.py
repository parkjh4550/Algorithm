# https://programmers.co.kr/learn/courses/30/lessons/43104

def solution(N):
    answer = 0
    tile = [1, 1]
    if N == 1:
        return tile[0] * 4
    if N == 2:
        return (tile[0] + tile[1]) * 2 + (tile[1]) * 2
    for itr in range(2, N):
        next_tile = tile[-1] + tile[-2]
        # print(next_tile)
        tile.append(next_tile)

    return (tile[-1] + tile[-2]) * 2 + (tile[-1]) * 2
