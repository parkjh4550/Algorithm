#https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3
def solution(tickets):
    # 끝지점을 찾은 후에 역으로 시작지점까지 찾는 방법이다.
    # 이는 모든 경로가 반드시 연결된다는 가정이 있기 때문에 가능함.
    # 또한 모든 지점을 지나는 경우가 반드시 있기 때문.
    # DSF  형식
    #build graph
    graph = {}
    for t in tickets:
        graph[t[0]] = graph.get(t[0], []) + [t[1]]
    for k in graph:
        graph[k].sort(reverse=True)

    stack=["ICN"]
    path = []

    while len(stack) > 0:
        current = stack[-1]
        if current not in graph or len(graph[current]) == 0:
            #현재 노드가 끝지점이면  path에 추가.
            path.append(stack.pop())
        else:
            #현재 노드가 다른 지점으로 이어진다면 그 지점을  stack에 추가.
            stack.append(graph[current][-1])
            graph[current] = graph[current][:-1]

    return path[::-1]

print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))

"""
# 이 경우에는 모든 경로를 다 쓰기 전에 마쳐버려서 테스트 케이스 1,2가 안된다.
def solution(tickets):
    answer = []
    path = ["ICN"]
    current = "ICN"
    #for itr in range(len(tickets)):
    while tickets:
        dest = [t for t in tickets if t[0]==current]
        print('---------------------')
        print('current : ', current)
        print(tickets)
        print(dest)
        print(path)
        print('---------------------')
        if not dest:
            if current == path[-2]: break
            current = path[-2]
            continue
        
        dest.sort(key= lambda x: x[1])
        current = dest[0][1]
        path.append(current)
        
        tickets.remove(dest[0])
        
    return path

print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]))
"""

