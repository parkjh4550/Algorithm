"""
# solve 1. use WFS
def WFS(c_graph, start, v_graph):
    queue = list()
    visit = list()

    queue.append(start)
    result = {start : v_graph[start]}   # result of value adding
    while queue:
        current_node = queue.pop(0)
        if current_node not in visit:
            # update v_graph
            if current_node != start:
                prev_nodes = list(map(int, c_graph[current_node]))
                for prev_node in prev_nodes:
                    if prev_node< int(current_node):
                        new_value = int(v_graph[current_node]) + int(result[str(prev_node)])
                        if current_node in result:
                            if int(result[current_node]) < new_value: result[current_node] = new_value
                        else:
                            result[current_node] = new_value
            # find adjecent node
            visit.append(current_node)
            queue.extend(c_graph[current_node])

    return result

size = int(input())
tri_values = []
tri_node = []
cnt = 0
for itr in range(size):
    input_list = list(input().split(' '))
    tri_values.append(input_list)
    tmp = []
    for itr2 in range(len(input_list)):
        tmp.append(str(cnt))
        cnt+=1
    tri_node.append(tmp)

# build connection graph
c_graph = {}
v_graph = {}
itr = 0
for l_itr, value in enumerate(tri_values):
    if l_itr == 0:
        v_graph['0'] = value[0][0]
        continue
    # add connection and value
    for n_itr, node in enumerate(tri_node[l_itr]):
        for itr in range(0,2):
            prev_index = n_itr - itr
            if prev_index>=0 and prev_index<len(tri_node[l_itr-1]):
                prev_node = tri_node[l_itr-1][prev_index]
                # prev_node info
                if prev_node in c_graph:
                    c_graph[prev_node].append(node)
                else:
                    c_graph[prev_node] = [node]
                # current node info
                if node in c_graph:
                    c_graph[node].append(prev_node)
                else:
                    c_graph[node] = [prev_node]

        v_graph[node] = tri_values[l_itr][n_itr]

v_graph = WFS(c_graph=c_graph, start='0', v_graph=v_graph)

max_v = max([v_graph[index] for index in tri_node[-1]])
print(max_v)
"""

# solve 2. only use adding function


size = int(input())
tri_values = []
for itr in range(size):
    input_list = list(map(int,input().split(' ')))
    tri_values.append(input_list)

result = [tri_values[0]]
for itr in range(1, len(tri_values)):
    tmp = []
    for itr2 in range(0, len(tri_values[itr])):
        for r in range(2):
            prev_index = itr2 - r
            if prev_index>=0 and prev_index<len(tri_values[itr-1]):
                new_value = tri_values[itr][itr2] + result[itr-1][prev_index]

                if len(tmp)-1 == itr2:
                    if new_value>tmp[itr2]: tmp[itr2] = new_value
                else:
                    tmp.append(new_value)
    result.append(tmp)

print(max(result[-1]))