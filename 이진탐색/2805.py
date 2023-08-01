# 1.아이디어
# for 2번 돌려서 최대 높이에서 한 번, trees에서 for 한 번
# n*m = 10^15 => 절대 안 됌

# 2.시간복잡도

# N, M = map(int, input().split())
# Trees = list(map(int, input().split()))


# def func(m, trees):

#     # 나무의 최대 높이를 설정
#     maxH = 0

#     # 가져간 나무 길이
#     takenH = 0
#     for element in trees:
#         maxH = max(maxH, element)

#     for i in range(1, maxH):
#         for each in trees:
#             if (maxH-i) < each:
#                 takenH += each - (maxH-i)

#         if takenH >= m:
#             wantedH = maxH - i
#             return wantedH

#         else:
#             takenH = 0


# print(func(M, Trees))

# 1.아이디어
# 이진 탐색을 이용해 1과 나무 최대 높이 사이에
# 통나무 높이를 찾으면 됌

# 2.시간복잡도
# n* log(m) = 10^6 * 9 * log(2) ~ 10^7 < 10^8


# N, M = map(int, input().split())
# Trees = list(map(int, input().split()))


# st, en = 1, max(Trees)


# def binSearch(start, end, trees, m):
#     if (start == end):
#         return start

#     total = 0

#     mid = (start + end) // 2

#     for tree in trees:
#         total += tree - mid

#     if total >= m:
#         binSearch(mid+1, end, trees, m)

#     else:
#         binSearch(start, mid, trees, m)


# print(binSearch(st, en, Trees, M))


N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)  # 이분탐색 검색 범위 설정

while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2

    log = 0  # 벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid

    # 벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
