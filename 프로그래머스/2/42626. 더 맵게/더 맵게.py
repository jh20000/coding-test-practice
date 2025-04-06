import heapq

def solution(scoville, K):

    cnt = 0

    heapq.heapify(scoville)

    while len(scoville) >= 2:
        mini = heapq.heappop(scoville)
        if mini >= K:
            return cnt
                   
        mini2 = heapq.heappop(scoville)
        new = mini + 2 * mini2
        heapq.heappush(scoville, new)
        cnt += 1

    #마지막 하나 남았을 때 검사
    if scoville and scoville[0]>=K:
        return cnt
    else:
        return -1