# 1.아이디어

# 뱀이 움직인다
# 사과가 있다
# 게임이 종료한다
# 몇 초에 끝나는지 출력한다

# i초마다 뱀이 움직인다
#   만약 i초에 방향 변환이 있을 때, i == X일 때
#     그 방향대로 뱀의 머리를 움직인다
#     머리를 움직였을 때
#       그 자리에 사과가 있으면
#         범위 안에 있고 뱀 리스트와 사과 리스트가 같지 않으면
#           사과의 좌표를 뱀에 리스트에 append

#         else
#           종료

#       사과가 없으면
#         이동범위 안에 있고 뱀 리스트와 리스트가 같지 않으면
#           이동하는 방향으로 뱀의 모든 리스트 요소값을 수정해준다

#   그 밖에 경우(방향변환이 없을 때) 전 방향 그대로 머리를 움직인다
#     머리를 움직였을 때
#       그 자리에 사과가 있으면
#         사과의 좌표를 뱀에 리스트에 append

#       사과가 없으면
#         이동하는 방향으로 뱀의 모든 리스트 요소값을 수정해준다


# 2번째도 실패해서 gpt한테 짜주라고 했음

from collections import deque

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

# place apples on the board
for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

l = int(input())
directoins = {}
for _ in range(l):
    x, c = input().split()
    directoins[int(x)] = c

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def simulate():
    direction = 1
    x, y = 0, 0
    time = 0

    snake = deque([x, y])

    while True:
        nx = x + dy[direction]
        ny = y + dy[direction]

        # check if the snake hits the wall or itself
