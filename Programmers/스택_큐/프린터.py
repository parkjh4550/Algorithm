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

def solution2(priorities, location):
    answer = 0
    while (True):
        answer += 1
        max_prior_value = max(priorities)
        max_prior_idx = priorities.index(max_prior_value)

        if max_prior_idx == location:
            break
        elif location < max_prior_idx:
            location = len(priorities) + location - max_prior_idx - 1
        elif location > max_prior_idx:
            location = location - max_prior_idx - 1

        if max_prior_idx == len(priorities) - 1:
            priorities = priorities[:max_prior_idx]
        else:
            priorities = priorities[max_prior_idx + 1:] + priorities[:max_prior_idx]

    return answer

if __name__ == '__main__':
    solution([2, 1, 3, 2], 2)