# 25.02.14 백준 DFS & BFS 기초 문제
# 처음 보는 문제여서 결국 도움 좀 받음..ㅠㅠ
# 조합으로 풀었다가 해결이 안돼서 보니 이것도 BFS를 사용할 수 있네.

import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
n, k = map(int, input().split())

MAX = 10 ** 5
visited = [0] * (MAX + 1)

def bfs(s):
    q = deque()
    q.append(s)

    while q:
        cur = q.popleft()
        if cur == k:
            return visited[k]
        for i in (cur+1, cur-1, cur * 2):
            if 0 <= i <= MAX and not visited[i]:
              visited[i] = visited[cur] + 1
              q.append(i)

print(bfs(n))