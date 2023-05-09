from collections import deque

def dfs(graph, v, visited): #DFS
    visited[v] = True #현재 방문한 노드를 방문처리

    for i in graph[v]:
        if not visited[i]: #해당 노드에 연결된 노드 중 방문하지 않은 노드로 방문
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start]) #BFS를 구현하기 위해 queue 생성
    visited[start] = True #시작노드 방문처리

    while queue:
        v = queue.popleft() #최근에 방문한 노드 popleft()

        for i in graph[v]: 
            if not visited[i]: #해당 노드랑 연결된 노드 중 방문하지 않은 노드
                queue.append(i) #queue에 append
                visited[i] = True #방문처리

#노드는 대부분 1번부터 시작하므로 "노드의수 + 1"
visited = [False] * 9

#각 노드가 어디에 연결되어있는지 정보를 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
] 
