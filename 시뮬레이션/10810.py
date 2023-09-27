'''
1. 아이디어
시뮬레이션

2. 시간복잡도
N*M = 100^2

3. 자료구조
N, M  = int

'''

N, M = map(int, input().split())

basket = []

for _ in range(N):
    basket.append(0)

for _ in range(M):
    i, j, k = map(int, input().split())
    for a in range(i-1, j):
        basket[a] = k

output = ' '.join(map(str, basket))

print(output)
