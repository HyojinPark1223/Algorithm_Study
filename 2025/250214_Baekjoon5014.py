# 25.02.14 백준 DFS & BFS 기초 문제

import sys
sys.stdin = open("input.txt", 'r')

from collections import deque

f, s, g, u, d = map(int, input().split())

# 빌딩 건물인지 확인하기
def isBuilding(x):
    return 0 < x <= f

def bfs():
    count = [0] * (f + 1)
    q = deque()
    q.append(s)
    count[s] = 1

    while q:
        cur = q.popleft()
        if cur == g:
            return count[g] - 1

        nxt1 = cur + u
        nxt2 = cur - d

        if isBuilding(nxt1) and count[nxt1] == 0:
            count[nxt1] = count[cur] + 1
            q.append(nxt1)

        if isBuilding(nxt2) and count[nxt2] == 0:
            count[nxt2] = count[cur] + 1
            q.append(nxt2)
    return 'use the stairs'

print(bfs())
