#https://programmers.co.kr/learn/courses/30/lessons/49189?language=python3
"""
# DFS
def solution(n, edge):
    answer = 0

    # build graph
    graph = {}
    for conn in edge:
        start, end = conn[0], conn[1]
        if start not in graph:
            graph[start] = [end]
        else:
            if end not in graph[start]:
                graph[start].append(end)

        if end not in graph:
            graph[end] = [start]
        else:
            if start not in graph[end]:
                graph[end].append(start)

    result = {1:0}
    stack = [(1, [])]  # (current, past)
    while stack:
        current = stack.pop()
        start = current[0]

        for path in graph[start]:
            prev_len = len(stack)
            if path not in current[1]:  # if the end not in the history, we can go there.
                stack.append([path, current[1] + [start]])

        if prev_len == len(stack):  # if there is no place to go, it's the end.
            dist = len(current[1])
            if start not in result:
                result[start]=dist-1
            else:
                if result[start]>dist:
                    result[start] = dist-1

    max_len = max(result.values())
    for m in result.values():
        if m == max_len: answer += 1

    return answer
"""
# BFS
from collections import defaultdict, deque

def bfs(start, tables, visited):
    queue = deque()
    queue.append((start,0))
    visited.add(start)

    # 가장 먼 노드의 개수를 세는 dictionary
    numbers = defaultdict(lambda :0)

    while queue:
        node, cnt = queue.popleft()
        visited.add(node)
        for neighbor in tables[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                numbers[cnt+1] +=1
                queue.append((neighbor, cnt+1))
    return numbers[cnt]

def solution(n, edge):
    answer = 0

    # build graph
    graph = defaultdict(set)
    for a,b in edge:
        graph[a].add(b)
        graph[b].add(a)

    visited= set()
    return bfs(1, graph, visited)

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))