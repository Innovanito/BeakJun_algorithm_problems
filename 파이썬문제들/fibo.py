import time
li = []


def fibo(i):
    if i < 2:
        li.append(i)
    else:
        li.append(li[i-1]+li[i-2])

    st = time.time()


for i in range(30):
    li.append(fibo(i))
print(li)
print(time.time()-st)
