#https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0
    data = [ [p, loc] for loc, p in enumerate(priorities) ]

    itr = 1
    while True:
        cur_p = data.pop(0)
        #end condition
        if cur_p[0] == max(priorities) and cur_p[1] == location:
            return itr
        # if not max prior, go to the back
        if cur_p[0] != max(priorities):
            data.append(cur_p)
            continue

        # pop data is max value
        priorities.pop(priorities.index(max(priorities)))
        itr+=1