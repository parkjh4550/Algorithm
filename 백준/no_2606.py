def DFS(graph, start):
    stack = list()
    visit = list()

    stack.append(start)

    while stack:
        current_node = stack.pop()

        if current_node not in visit:
            visit.append(current_node)
            stack.extend(graph[current_node])
    return visit

num_computer = int(input())
num_connection = int(input())

graph = {}
connection = [input().split(' ') for itr in range(0,num_connection)]

# build graph
for start, end in connection:
    # add start node
    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]

    # add end node
    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]

#for k in graph.keys():
#    print(k, ' : ', graph[k])
# DFS algorithm
visit = DFS(graph=graph, start = '1')

#print(visit)
# count the number of computers except the start one
print(len(visit[1:]))