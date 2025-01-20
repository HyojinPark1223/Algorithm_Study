# 독감으로 인해 코테 공부 하자마자 1일 1문제 못함.. 반성..ㅠㅠ 몸관리 열심히 하기,,
# 25.01.20 백준 DFS & BFS 기초 문제
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')

n = int(input())
tc = int(input())

# 연결된 컴퓨터를 배열로 받아둠. 편한 계산을 위해 n+1개의 배열을 만들어서 바로 넣어줌
tree = [[] for _ in range(n + 1)]
checked = [0] * (n + 1)

for _ in range(tc):
    s, e = map(int, input().split())

    # 양방향 그래프이므로 양쪽에 넣어준다.
    # ※이 양방향으로 넣어주는 걸 맨날 안해서 트리 문제 런타임 에러가 나곤 하니 다음부터 주의하기.
    tree[s].append(e)
    tree[e].append(s)

# 1번 컴퓨터부터 시작
q = deque([1])
checked[1] = 1

while q:
    com = q.popleft()

    for node in tree[com]:
        if checked[node] == 0:
            q.append(node)
            checked[node] = 1

print(sum(checked) - 1)