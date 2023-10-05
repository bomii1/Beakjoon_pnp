## 1260

#### DFS (Depth-First Search, 깊이우선탐색)
#### BFS (Breadth-First Search, 너비우선탐색)

- 입력 값을 토대로 인접 행렬로 변환

```python
N, M, V = map(int, input().split())

matrix = [[0 for j in range(N+1)] for i in range(N+1)]
visitedD = [0] * (N+1) # DFS 방문 check
visitedB = [0] * (N+1) # BFS 방문 check

for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1
```

#### DFS
- matrix 를 돌면서 값이 1이고 이전에 방문하지 않았다면 방문 표시
```python
def DFS(V):
    visitedD[V] = 1 
    print(V, end=' ')
    for i in range(1, N+1):
        if matrix[V][i] == 1 and visitedD[i] == 0:
            DFS(i)
```

#### BFS
- collections 모듈의 deque 사용 
- matrix 를 돌면서 값이 1이고 이전에 방문하지 않았다면 방문 표시
```python
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
```


