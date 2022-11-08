from copy import deepcopy


def coin_change(change):
    coin = [500, 100, 80, 50, 10, 5, 1]
    lst_change = [999] * (change + 1)
    lst_change[0] = 0
    lst_coin = [[]] * (change + 1)
    for j in range(1, change+1):
        lst_coin[j] = []
        for i in coin:
            if i <= j and lst_change[j-i] + 1 < lst_change[j]:
                print('lst_change[j]', lst_change[j])
                lst_change[j] = lst_change[j-i]+1
                lst_coin[j] = deepcopy(lst_coin[j-i])

                lst_coin[j].append(i)
    return lst_change, lst_coin


money = int(input('거스름돈 입력:'))
num_coins, used_coins = coin_change(money)

for i in range(money+1):
    print('%3d' % i, end=' ')
print()
for i in range(money+1):
    print('%3d' % num_coins[i], end='')
print()
print('거스름돈 %d에 대한 최소 동전 수 = %d' % (money, num_coins[money]))

print('사용된 동전:', used_coins[money])
