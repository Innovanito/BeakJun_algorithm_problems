'''
1.아이디어
가장 큰 동전을 기준으로 몇 개 사용하냐에 다라 트리 구조의 경우의 수가 생기는 듯

2. 시간복잡도

3.지료그조
coins : int[]
n, k : int
'''

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
