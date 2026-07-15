from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
           
    visited= [[0] * m for _ in range(n)]
    
    queue = deque()
    queue.append((0,0))
    visited[0][0] = 1
    
    directions = [(-1,0), (1,0),(0,-1),(0,1)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if (0<=nx<=n-1) and (0<=ny<=m-1) and (maps[nx][ny] == 1) and (visited[nx][ny] == 0):
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    if visited[n-1][m-1] == 0:
        return -1
    else:
        return visited[n-1][m-1]
