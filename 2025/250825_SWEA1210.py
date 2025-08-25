# 25.08.25 SWEA 1210. [S/W 문제해결 기본] 2일차 - Ladder1
# D3는 너무 간단하게 풀려서 D4 공부 시작(D3 노트북 빌려 공부해서 코드가 없다..ㅠㅠ)

import sys
sys.stdin = open("input.txt", 'r')

d = [(0, -1), (0, 1), (-1, 0)]  # 제일 아래지점부터 올라가니 탐색 방향은 좌, 우, 위
def find_x(x, y):
    if x == 0:
        return y
        
    # 이동 경로 표시
    visited[x][y] = 1
    nx, ny = -1, -1
    for dx, dy in d:
        nx = x + dx
        ny = y + dy

        # 한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다고 하였으니, 이동하면 break
        if 0<= nx < 100 and 0 <= ny < 100 and not visited[nx][ny] and ladder[nx][ny] == 1:
            break
    return find_x(nx, ny)

for t in range(10):
    tc = int(sys.stdin.readline())
    ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    
    # 끝 포인트에서 위로 올라가서 최종 값을 return하면 됨.
    start = ladder[99].index(2)
    print(f"#{tc} {find_x(99, start)}")
