def binarySearch(array, target, left, right):
    global searchTime
    searchTime += 1
    middle_idx = (left+right)//2
    print(middle_idx)
    middle = array[middle_idx]
    if searchTime > len(array):
        print('찾는 값이 없습니다.')
        return False
    else:
        if target == middle:
            print('answer {}'.format(middle_idx))
        elif middle > target:
            binarySearch(array, target, left, middle_idx-1)
        elif middle < target:
            binarySearch(array, target, middle_idx+1, right)
        else:
            return False


searchTime = 0
target = int(input('찾고자 하는 값:'))
m_list = [30, 94, 27, 92, 21, 37, 25, 47, 25, 53, 98, 19, 32, 32, 7]
length = len(m_list)

m_list.sort()
left = 0
right = length-1

binarySearch(m_list, target, 0, right)


# li = [2, 3]


# def fibo(i):
#     if i < 2:
#         return li[i]
#     else:
#         return li[i-1]+li[i-2]


# max = int(input('몇번째 피보나치 수열을 구하시겠습니까?'))
# for i in range(max):
#     li.append(fibo(i))
# print(li)
