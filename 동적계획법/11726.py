'''
1.아이디어
-점화식 : An = An-1 + An-2 => 피보나치 수열
-N값 구하기 위해, for 3부터 N까지 값을 구해주기
-이전값과 그 이전값을 더해, 10007을 나눠 저장

2.시간복잡도
-O(N)

3.자료구조
-DP값 저장하는 경우의 수 배열: int[] => 최대값은 10007
'''

import sys
input = sys.stdin.readline

N = int(input())

n = int(input())
