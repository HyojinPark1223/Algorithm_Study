# 25.09.04 SWEA 3124. 최소 스패닝 트리
# 다른 말로 최소 신장 트리. Spanning Tree란 그래프 내의 모든 정점을 포함하는 트리임. 최소 스패닝 트리라는건 이 연결된 정점이 최소인 경우.

import sys
sys.stdin = open("input.txt", "r")

def find_parent(parent ,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_find(parent, a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

t = int(input())
for tc in range(1, t+1):
    node, edge = map(int, input().split())
    graph = []
    for i in range(edge):
        a, b, cost = map(int, input().split())
        graph.append([cost, a, b])
    graph.sort()

    parent = [0] * (node+1)
    for i in range(1, node+1):
        parent[i] = i
    costs = 0
    for i in range(edge):
        cost, a, b = graph[i]
        a_parent = find_parent(parent, a)
        b_parent = find_parent(parent ,b)
        if a_parent != b_parent:
            union_find(parent, a_parent, b_parent)
            costs += cost
    print(f'#{tc} {costs}')