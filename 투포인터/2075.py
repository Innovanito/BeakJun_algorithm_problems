'''
1. 아이디어
queue를 사용해 N*N의 수들을 정렬해버리기 => 이렇게 하면 안됌
왜냐하면 arr의 요소가 2백만이 되기 때문에 공간복잡도가 초과하기 때문
공간복잡도는 최대 백만이 기준임

heap을 이용해서 값을 저장해야 함

2. 시간복잡도
N^2 = 1500^2 = 2,250,000

3. 자료구조
N = int
q = deque()
numList = int[][]


'''

import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if len(heap) == N:
            a = heapq.heappop(heap)
            if a < arr[j]:
                heapq.heappush(heap, arr[j])
            else:
                heapq.heappush(heap, a)

        else:
            heapq.heappush(heap, arr[j])

print(heapq.heappop(heap))
