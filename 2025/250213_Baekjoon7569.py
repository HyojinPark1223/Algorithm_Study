# 25.02.13 백준 DFS & BFS 기초 문제
# 3차원 배열을 이용하기... 제일 약한 문제..ㅠㅠ 하지만 풀이 안보고 해결했다!! 성장했따!!!
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
m, n, h = map(int, input().split())

box = []
for _ in range(h):
    temp = []
    for i in range(n):
        temp.append(list(map(int, input().split())))
    box.append(temp)

# 처음 익은 토마토의 좌표를 적어준다.
tomato = []
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                tomato.append((i, j, k))

#BFS를 이용해서 동시에 좌표를 구하기
d = [(0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1), (1, 0, 0), (-1, 0, 0)]   # 총 방향 정보

def inBox(x, y, z):
    if 0 <= x < m and 0 <= y < n and 0 <= z < h:
        return True
    return False

def bfs():
    global tomato, box
    q = deque()
    q.extend(tomato)

    while q:
        h, n, m = q.popleft()
        for dh, dy, dx in d:
            nh = dh + h
            nn = dy + n
            nm = dx + m

            # 박스 안의 토마토일 때, 익지 않은 토마토라면 확인
            if inBox(nm, nn, nh) and box[nh][nn][nm] == 0:
                # 인근의 토마토는 다음 날 익을테니 현재 상태에서 + 1을 해주고 queue에 넣어줌
                box[nh][nn][nm] = box[h][n][m] + 1
                q.append((nh, nn, nm))

bfs()
answer = -1

# 박스를 돌며 확인
for i in range(h):
    for j in range(n):
        # 안 익은 토마토가 있으면 -1 출력하고 종료
        if 0 in box[i][j]:
            print(-1)
            exit()
        # 익은것 뿐이라면 가장 큰 수를 저장
        answer = max(max(box[i][j]), answer)
# 다 익은 날짜를 체크할 것이므로 -1을 해줘야됨.
print(answer - 1)