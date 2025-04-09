import heapq

def solution(jobs):
    # 작업 번호 포함시키기
    for idx, (req, dur) in enumerate(jobs):
        jobs[idx] = (req, dur, idx)
    jobs.sort()
    
    heap = []
    time = 0
    idx = 0
    count = 0
    total_time = 0

    while count < len(jobs):
        while idx < len(jobs) and jobs[idx][0] <= time:
            req, dur, job_idx = jobs[idx]
            heapq.heappush(heap, (dur, req, job_idx))
            idx += 1

        if heap:
            dur, req, job_idx = heapq.heappop(heap)
            time += dur
            total_time += time - req
            count += 1
        else:
            time = jobs[idx][0]

    return total_time // len(jobs)
