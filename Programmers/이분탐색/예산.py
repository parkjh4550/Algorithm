#https://programmers.co.kr/learn/courses/30/lessons/43237?language=python3#


def solution(budgets, M):
    answer = 0

    if M >= sum(budgets):
        return max(budgets)

    budgets.sort()
    num_regions = len(budgets)

    max_d, min_d = max(budgets),0
    mid, new_mid = 0, 0
    while True:
        new_mid = int((min_d + max_d) / 2)
        new_bud = [new_mid if b > new_mid else b for b in budgets]

        if mid == new_mid and sum(new_bud) <= M:
            break

        if M > sum(new_bud):  # it can be larger
            min_d = new_mid
            # mid = sum(budgets[ind:])/len(budgets[ind:])

        elif M < sum(new_bud):  # it must be smaller
            max_d = new_mid
        mid = new_mid
        answer = new_mid

        """
        if mid == new_mid and sum(new_bud) <= M:
            break


        answer = new_mid

        if M > sum(new_bud):  # it can be larger
            min_d = new_mid
            # mid = sum(budgets[ind:])/len(budgets[ind:])

        elif M < sum(new_bud):  # it must be smaller
            max_d = new_mid
        mid = new_mid
        # mid = sum(budges[:ind+1])/len(budgets[:ind+1])
    """
    return answer

print(solution([120, 110, 140, 150], 485))