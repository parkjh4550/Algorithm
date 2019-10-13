# not only find the path, it also return cost

def solve_maze(g, start, end):
    queue = []
    visit = []
    cost_q = []

    queue.append(start)
    cost_q.append(0)
    while queue:
        current_p = queue.pop(0)
        current_cost = cost_q.pop(0)
        #if end in queue:
            #return 'find'
        if current_p == end:
            return 'find', current_cost
        if current_p not in visit:
            queue.extend(g[current_p])
            cost_q.extend([current_cost+1 for itr in range(len(g[current_p]))])
            visit.append(current_p)
    return 'impossible'


maze ={
    'a' : ['e'],
    'b' : ['c', 'f'],
    'c' : ['b', 'd'],
    'd' : ['c'],
    'e' : ['a', 'i'],
    'f' : ['b','g','j'],
    'g' : ['f', 'h'],
    'h' : ['g', 'l'],
    'i' : ['e', 'm'],
    'j' : ['f', 'k', 'n'],
    'k' : ['j','o'],
    'l' : ['h','p'],
    'm' : ['i','n'],
    'n' : ['m', 'j'],
    'o' : ['k'],
    'p' : ['l']
}

print(solve_maze(maze, 'a', 'p'))