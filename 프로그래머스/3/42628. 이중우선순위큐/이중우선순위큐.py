import heapq

def solution(operation):
    min_heap = []
    max_heap = []
    idx = 0
    visited = dict()
    
    for op in operation:
        if op[0] == 'I':
            num = int(op[2:])
            heapq.heappush(min_heap, (num, idx))
            heapq.heappush(max_heap, (-num, idx))
            visited[idx] = True
            idx += 1  # 고유 인덱스 증가

        elif op == 'D 1':
            while max_heap and not visited.get(max_heap[0][1], False):
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)

        elif op == 'D -1':
            while min_heap and not visited.get(min_heap[0][1], False):
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)

    # 연산 끝난 뒤: 유효하지 않은 값들 제거
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)

    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)

    if not max_heap or not min_heap:
        return [0, 0]
    
    return [-max_heap[0][0], min_heap[0][0]]
