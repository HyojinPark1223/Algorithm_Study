# 25.02.14 백준 DFS & BFS 기초 문제
# 문제 이해가 되지 않아서(안전 영역의 개수 카운팅이 이해가 되지 않아서...) 다른 사람 풀이 봄.ㅠ
# 인접한 지역이라는게 일단 붙어있는 모든 영역의 개수를 뜻했다. 지난번에 단지수 붙이기랑 동일한 방식으로 해결 가능.

import sys
sys.stdin = open("input.txt", 'r')

from collections import deque

n = int(input())
graph = []
maxNum = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > maxNum:
            maxNum = graph[i][j]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(sx, sy, value, visited):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


result = 0
for i in range(0, maxNum):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i, visited)
                cnt += 1

    if result < cnt:
        result = cnt

print(result)
