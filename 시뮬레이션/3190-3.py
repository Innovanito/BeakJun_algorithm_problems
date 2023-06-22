from collections import deque

n = int(input())
k = int(input())

board = [[0] * n for _ in range(n)]

for _ in range(k):
    row, col = map(int, input().split())
    board[row-1][col-1] = 1

l = int(input())
directions = {}
for _ in range(l):
    x, c = input().split()
    directions[int(x)] = c

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def simulate():
    direction = 1
    x, y = 0, 0
    time = 0

    snake = deque([(x, y)])

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
            return time + 1

        snake.append((nx, ny))

        if board[nx][ny] == 1:
            board[nx][ny] = 0

        else:
            snake.popleft()

        x, y = nx, ny

        if time+1 in directions:
            if directions[time+1] == 'D':
                direction = (direction+1) % 4
            else:
                direction = (direction-1) % 4

        time += 1


print(simulate())


'''
from collections import deque

# Read the input values
n = int(input())  # Size of the board
k = int(input())  # Number of apples

# Initialize the board with all empty spaces
board = [[0] * n for _ in range(n)]

# Place the apples on the board
for _ in range(k):
    row, col = map(int, input().split())
    board[row - 1][col - 1] = 1

# Read the number of direction changes and their corresponding time
l = int(input())
directions = {}
for _ in range(l):
    x, c = input().split()
    directions[int(x)] = c

# Define the directions (up, right, down, left)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def simulate():
    direction = 1  # Initial direction: right
    x, y = 0, 0  # Initial position: top-left corner
    time = 0  # Initial time

    # Queue to store the snake's body positions
    snake = deque([(x, y)])

    # Start the simulation loop
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        # Check if the snake hits the wall or itself
        if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
            return time + 1
        
        # Move the snake to the next position
        snake.append((nx, ny))

        # Check if the snake eats an apple
        if board[nx][ny] == 1:
            board[nx][ny] = 0  # Remove the apple
        else:
            snake.popleft()  # Remove the tail of the snake
        
        # Update the current position
        x, y = nx, ny

        # Check if it's time to change the direction
        if time + 1 in directions:
            if directions[time + 1] == 'D':  # Turn right
                direction = (direction + 1) % 4
            else:  # Turn left
                direction = (direction - 1) % 4
        
        # Increment the time
        time += 1

# Run the simulation and print the result
print(simulate())

'''
