# https://programmers.co.kr/learn/courses/30/lessons/12977?language=python3
def is_prime(sum):
    i = 2
    while i < sum:
        if i*i >sum: break
        if sum%i == 0:
            return False
        i+=1
    return True

def solution(nums):
    answer = 0
    len_num = len(nums)
    for itr1, first in enumerate(nums[:-2]):
        for itr2 in range(itr1+1, len_num-1):
            for itr3 in range(itr2+1, len_num):
                sum = first+nums[itr2]+nums[itr3]
                if is_prime(sum): answer+=1

    return answer


print(solution([1,2,3,4]))