import heapq

arr = [[1, 3], [3, 1]]

arr2 = [2, 0]

heapq.heappush(arr, arr2)

print(arr)


heapq.heappop(arr)
heapq.heappop(arr)
print(arr)
