# 25.01.20 백준 DFS & BFS 기초 문제
'''
예전에 풀어본 적 있었던 알고리즘 문제여서 제출 한 방에 바로 해결했다.
이 알고리즘 법의 이름을 어디서 봤었던 기억이 나는데 찾아보려니까 나오지 않는다..ㅠㅠ
메모리 활용상 deque를 이용한 BFS로 푸는게 정석이라고 생각하는데, dfs 방법도 있나 싶어서 찾아봤고
다른 사람의 풀이를 보긴 했지만 dfs로도 해결했다.
'''
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

house = []

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# BFS를 이용하되, 외부에서 한 번 더 for문을 사용하여 근처의 집 개수를 찾는 알고리즘 적용으로 해결해야 됨.

def isBound(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(startx, starty):
    global visited, house

    cnt = 0
    q = deque([(startx, starty)])
    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in d:
            nx = x + dx
            ny = y + dy

            if isBound(nx, ny) and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    house.append(cnt)

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            bfs(i, j)

house.sort()
print(len(house))
for i in house:
    print(i)

# DFS
def DFS(x, y):
    if isBound(x, y) and arr[x][y] == 1:
        global count
        count += 1
        arr[x][y] = 0
        for dx, dy in d:
            nx = x + dx
            ny = y + dy
            DFS(nx, ny)
        return True
    return False

count = 0
result = 0
num = []

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0