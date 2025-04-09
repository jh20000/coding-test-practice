import heapq

def solution(jobs):
    jobs.sort()  # 요청 시각 기준 정렬
    heap = []
    
    time = 0  # 현재 시각
    idx = 0   # jobs 리스트 인덱스
    total_time = 0
    count = 0
    
    while count < len(jobs):
        # 현재 시간까지 요청된 작업들을 모두 heap에 넣음
        while idx < len(jobs) and jobs[idx][0] <= time:
            req, dur = jobs[idx]
            heapq.heappush(heap, (dur, req))  # 소요시간 기준 우선순위 큐
            idx += 1

        if heap:
            dur, req = heapq.heappop(heap)
            time += dur  # 현재 작업 끝나는 시간
            total_time += time - req  # 반환 시간 누적
            count += 1
        else:
            # 아직 들어온 작업이 없는 경우 -> 다음 작업 시각으로 시간 점프
            time = jobs[idx][0]

    return total_time // len(jobs)
