from collections import deque

def DFS(V):
    visitedD[V] = 1
    print(V, end=' ')
    for i in range(1, N+1):
        if matrix[V][i] == 1 and visitedD[i] == 0:
            DFS(i)

def BFS(V):
    queue = deque()
    queue.append(V)
    visitedB[V] = 1

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in range(1, N+1):
            if matrix[node][i] == 1 and visitedB[i] == 0:
                queue.append(i)
                visitedB[i] = 1

N, M, V = map(int, input().split())

matrix = [[0 for j in range(N+1)] for i in range(N+1)]
visitedD = [0] * (N+1)
visitedB = [0] * (N+1)

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

DFS(V)
print()
BFS(V)


