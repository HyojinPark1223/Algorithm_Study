# 25.01.11 백준 DFS & BFS 기초 문제
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

#min_ans = 10001  #100*100로 최소값 계산을 했지만 arr 자체에 값을 넣어줄 거라서 BFS에서는 필요 없음.
q = deque()
q.append((0, 0))

def inBox(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

while q:
    x, y = q.popleft()

    # 방향 이동
    for dx, dy in d:
        nx, ny = x + dx, y + dy

        # 다음으로 넘어갈 위치 확인
        if inBox(nx, ny) and arr[nx][ny] == 1:
            arr[nx][ny] = arr[x][y] + 1
            q.append((nx, ny))

print(arr[n-1][m-1])
'''
# 미로 찾기라 dfs로 문제 풀이를 했는데, 시간초과에 걸렸다.
# 재귀를 돌리면서 런타임이 길어진듯 하여, deque를 사용해서 런타임을 줄일 수 있게 bfs로 변경하였다.
# 아래는 dfs 코드 
def dfs(x, y, path):
    global min_ans
    
    # 배열의 끝에 도착하면 지금까지의 길이를 비교하여 최소값 저장
    if x == (n-1) and y == (m-1):
        if path < min_ans:
            min_ans = path
        return
    
    # 방향을 돌리면서 배열의 값이 1이고, 방문하지 않은 곳이면 다시 재귀 호출
    for dx, dy in d:
        nx, ny = x + dx, y + dy

        if inBox(nx, ny) and not visited[nx][ny] and arr[nx][ny] == 1:
            visited[nx][ny] = True
            dfs(nx, ny, path + 1)
            visited[nx][ny] = False

visited[0][0] = True
dfs(0, 0, 1)

print(min_ans)
'''