# input graph
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D', 'G'],
    'D': ['C', 'E'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def BFS(graph, start_node):
    visit = list()
    queue = list()
    queue.append(start_node)

    cnt = 0
    while queue:
        print(str(cnt) + ' : ', queue)

        current_node = queue.pop(0)
        if current_node not in visit:
            visit.append(current_node)
            queue.extend(graph[current_node])
        cnt+=1

    return visit

def DFS(graph, start_node):
    visit = list()
    stack = list()
    stack.append(start_node)

    cnt = 0
    while stack:
        print(str(cnt) + ' : ', stack)
        current_node = stack.pop()
        if current_node not in visit:
            visit.append(current_node)
            stack.extend(graph[current_node])
        cnt+=1
    return stack

if __name__ == '__main__':
    BFS(graph=graph, start_node='A')
    DFS(graph=graph, start_node='A')