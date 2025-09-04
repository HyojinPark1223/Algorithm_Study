# 25.09.03 SWEA 1249. [S/W 문제해결 응용] 4일차 - 보급로
# BFS 문제. 현재 지점에서 방문하지 않은 곳의 합을 더해서 최종에 도착했을 때 최솟값을 구하면 될 듯함.(살짝 DP)
# 근데 주변 점들 중 가장 적은 점으로(동일한 값이면 두번 넣으면) 더 빠르지 않을까 싶어서 이걸 우선으로 해봤는데 안됨..ㅠ

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    visited = [[1e5] * n for _ in range(n)]
    # 큰 수를 나타낼때 1e5(10의 5제곱)을 사용함

    q = deque([(0, 0)])
    visited[0][0] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0), (0, 1), (0, -1), (1, 0)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n: # 범위 벗어나면 안됨
                if visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    q.append((nx, ny))

    print(f"{t} {visited[n-1][n-1]}")