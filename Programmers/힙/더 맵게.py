#https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    scoville = [scoville[i] for i in range(0, len(scoville)) if scoville[i] <=K]
    try:
        while True:
            if scoville[0] <= K:
                heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville)*2))
                answer+=1
            else:
                 break
    except:
        return -1
    return answer