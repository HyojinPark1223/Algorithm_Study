# 25.04.01 코드 트리 미지의 공간 탈출
# 업무 너무 바쁘다.. 일하면서 코딩 공부 어케 하는거야... 대단한 사람들!

import sys
sys.stdin = open("input.txt", 'r')

N, M, F = map(int, input().split())
d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 전체 평면도
arr = [list(map(int, input().split())) for _ in range(N)]

# 동, 서, 남, 북, 윗면
e_map = [list(map(int, input().split())) for _ in range(M)]
w_map = [list(map(int, input().split())) for _ in range(M)]
s_map = [list(map(int, input().split())) for _ in range(M)]
n_map = [list(map(int, input().split())) for _ in range(M)]
t_map = [list(map(int, input().split())) for _ in range(M)]

f = [list(map(int, input().split())) for _ in range(F)]     # r, c, d, v

# 시작점
start_point = ()
for i in range(M):
    for j in range(M):
        if t_map[i][j] == 2:
            start_point = (i, j)
            break
    if start_point != ():
        break

# 비상구 위치
escape_point = ()
# 타이머신이 시작하는점
machine_start = ()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 4:
            escape_point = (i, j)
        if arr[i][j] == 3 and machine_start == ():
            machine_start = (i, j)
    if escape_point != () and machine_start != ():
        break

###############################초기 셋팅###############################

