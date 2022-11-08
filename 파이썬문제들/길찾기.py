def is_valid(r, c):
    if 0 <= r < row and 0 <= c < col and\
            visited[r][c] == 0 and\
            maze[r][c] == 0:
        return True
    else:
        return False


def find_path(r, c):
    if r == row-1 and c == col-1:
        visited[r][c] = 1
        return True
    if is_valid(r, c):
        visited[r][c] = 1
        if find_path(r+1, c):
            return True
        if find_path(r, c+1):
            return True
        if find_path(r-1, c):
            return True
        if find_path(r, c-1):
            return True
        visited[r][c] = 0
        return False


maze = [
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 1, 1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

row = len(maze)  # 세로 열
col = len(maze[0])  # 가로 행
visited = [[0 for _ in range(col)] for _ in range(row)]  # 경로 저장
if find_path(0, 0):  # 출구를 찾았으면
    for i in visited:  # 경로 출력
        print(i)
else:
    print('경로 없음')
