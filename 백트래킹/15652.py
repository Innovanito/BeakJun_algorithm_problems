# 1.아이디어
# N파이M 했던 것에다가 비내림차순 조건만 추가해주면 될듯

# 2.시간복잡도
# 8! < 2억

# 3.자료구조
# N,M = int
# rst = []


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rst = []

# 첫 번째 풀이 => 시간초과
# def recur(num, lst):
#     if num == M:
#         if (M == 1):
#             rst.append(lst)
#             return
#         else:
#             for k in range(M-1):
#                 if (lst[k] <= lst[k+1]):
#                     if (k == M-2):
#                         rst.append(lst)
#                         return
#                 else:
#                     return

#     for j in range(1, N+1):
#         recur(num+1, lst + [j])


# recur(0, [])

def recur(num, start, lst):
    if num == M:
        rst.append(lst)
        return

    for j in range(start, N+1):
        recur(num+1, j, lst+[j])


recur(0, 1, [])


for singleLst in rst:
    print(*singleLst)
