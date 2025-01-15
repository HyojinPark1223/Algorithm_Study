# 25.01.11 백준 DFS & BFS 기초 문제
import sys
sys.stdin = open("input.txt", 'r')

n, m, v = map(int, input().split())

# 노드 연결
# 각 노드별로 연결되어 있는 정점을 표시해줬다.
# 불필요한 탐색시간 및 메모리를 줄이기 위해 N*N의 2차원 배열보다 연결된 정점만 표시해주는 2중 배열을 사용하려고 했으나,
# 노드가 직선형이 아닌 고리형인 관계로 N*N 2차원 배열 사용.

nodes = [[False]*n for _ in range(n)]

for i in range(m):
    s, e = map(int, input().split())
    nodes[s - 1][e - 1] = nodes[e - 1][s - 1] = True

# dfs
# dfs 깊이 탐색으로 연결된 정점들을 먼저 탐색한 뒤, 다시 올라와 다음 연결된 정점들을 쭉 탐색한다.
# 따라서 재귀함수를 사용(스택)
visited = [False] * (n + 1)
def dfs(V):
    print(V, end=' ')
    for i in range(n):
        if nodes[V-1][i] and not visited[i + 1]:
            visited[i + 1] = True       # 방문 처리
            dfs(i + 1)

visited[v] = True
dfs(v)
print()

# bfs
# bfs는 넓이 탐색으로 연결된 노드들을 먼저 훑는 dfs와 달리 같은 순위에 있는 노드들을 먼저 훑고 다음으로 넘어간다.
# 따라서 큐를 사용
q = [v]
visited2 = [False] * (n + 1)
visited2[v] = True

while q:
    node = q.pop(0)
    print(node, end=' ')
    for i in range(1, n + 1):
        if not visited2[i] and nodes[node - 1][i - 1]:
            q.append(i)
            visited2[i] = 1     # 방문처리