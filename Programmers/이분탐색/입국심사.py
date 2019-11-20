def solution(n, times):
    answer = 0

    times.sort()
    min_t, max_t = min(times), max(times)
    min_t, max_t = 0, max_t * n
    prev_mid = 0
    while True:
        mid = int((max_t + min_t) / 2)
        if prev_mid == mid:
            break

        customer = [mid//t for t in times]
        # = 부분에 주의 하자.
        # 둘 중 하나에 =를 붙이고, +1 혹은 -1 해주면서 바꾸어야 된다.
        if n > sum(customer):
            min_t = mid+1
        elif n <= sum(customer):
            max_t = mid

        """
        if n >= sum(customer):
            min_t = mid
        elif n < sum(customer):
            max_t = mid-1
        """
        prev_mid = mid

    return prev_mid

print(solution(6, [7, 10]))