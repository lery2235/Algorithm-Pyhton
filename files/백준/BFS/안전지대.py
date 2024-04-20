import sys
from collections import deque
sys.stdin = open("안전지대", "rt")

n = int(input())
board = [list(map(int, input().split()))for _ in range(n)]
max_count = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(i, j, rain):
    queue = deque()
    queue.append((i, j))
    # 상하좌우로 움직이며 안전 영역을 찾아낸다
    while queue:
        x, y = queue.popleft() # 현재 좌표를 꺼낸다.
        for dx, dy in ((1,0),(-1,0),(0,-1),(0, 1)): # 상하좌우 탐색
            nx, ny = x + dx, y + dy # 다음 위치 저장
            if in_range(nx, ny) and not visited[nx][ny] and board[nx][ny] > rain: # 다음 위치가 범위 안이고, 방문되지 않고 다음 위치가 비의 잠기지 않았다면
                visited[nx][ny] = True # 방문처리
                queue.append((nx, ny))  # 다음 위치를 큐에 넣는다.

for rain in range(100):# 비의 입력값 최대 100
    visited = [[False for _ in range(n)] for _ in range(n)] # 리스트 방문을 확인하는 리스트
    cnt = 0 # 안전지대 숫자를 세기 위한 카운트 변수
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] > rain: # 현재 지점이 방문되지 않았고, 비에 잠기지 않는 높이라면
                visited[i][j] = True # 현재 지점을 방문 처리
                bfs(i, j, rain) # 상하좌우 탐색
                cnt += 1
    max_count = max(max_count, cnt)

print(max_count)

