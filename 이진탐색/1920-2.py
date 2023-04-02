'''
1. 아이디어
-N개의 숫자를 정렬
-M개를 for 돌면서, 이진탐색
-이진탐색 안에서 마지막 데이터 찾으면, 1출력, 아니면 0 출력

2. 시간복잡도
-N개 입력값 정렬 = O(NlgN)
-M개를 N개 중에서 탐색 = O(MlgN)
총합 O((N+M)lgN)

3.자료구조
-N개 숫자: int[]
-M개 숫자: int[]
'''

import sys
input = sys.stdin.readline

M = int(input())
arr1 = list(map(int, input().split()))
N = int(input())
arr2 = list(map(int, input().split()))

arr1.sort()


def search(st, end, target):
    if st == end:
        if arr1[st] == target:
            print(1)
        else:
            print(0)
        return

    mid = (st+end) // 2
    if arr1[mid] < target:
        search(mid+1, end, target)
    else:
        search(st, mid, target)


for element in arr2:
    search(0, N-1, element)
