def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    def dfs(node):
        visited[node] = True
        for j in range(len(computers)):
            if computers[node][j] == 1:
                if visited[j] == False:
                    dfs(j)
    for i in range(n):
        if visited[i] == False:
            dfs(i)
            cnt += 1
    return cnt