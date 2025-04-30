from collections import deque

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    count = 1
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                count += 1
    return count

def solution(n, wires):
    answer = n  # 최대 차이는 n-1, 최소 차이는 0 → 초기값 크게 설정
    for i in range(len(wires)):
        temp = wires[:i] + wires[i+1:]  # 한 간선 제거
        graph = [[] for _ in range(n+1)]  # 1-based 인덱스
        
        # 그래프 구성
        for a, b in temp:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * (n+1)
        group_size = bfs(1, graph, visited)
        other_group = n - group_size
        diff = abs(group_size - other_group)
        answer = min(answer, diff)
        
    return answer
