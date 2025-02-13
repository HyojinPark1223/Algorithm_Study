# 25.02.13 백준 DFS & BFS 기초 문제
import sys

sys.stdin = open("input.txt", 'r')
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())

# 부모의 정보를 담을 nodes_p를 설정. 부모는 1명이므로 list 표현
nodes_p = [0] * n

for _ in range(m):
    p, c = map(int, input().split())
    nodes_p[c-1] = p

answer = -1

# 부모 list를 타고 올라가며, 뿌리에 도달할 때까지 정보를 담아줌.
p1_parents = [p1]
p_info = nodes_p[p1 - 1]
while p_info != 0:
    p1_parents.append(p_info)
    p_info = nodes_p[p_info - 1]

# 다른 자식의 부모 list도 탐색
p2_p = p2
cnt = 0
while p2_p != 0:
    # 이 때 이전에 구했던 p1의 부모가 겹친다면 거기까지가 촌수이므로 계산.
    if p2_p in p1_parents:
        idx = p1_parents.index(p2_p)
        answer = idx + cnt
        break
    p2_p = nodes_p[p2_p - 1]
    cnt += 1
# 겹치는 부모를 못 구했다면, -1 리턴
print(answer)