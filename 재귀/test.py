N = 5


def fun_a(level):
    if level == N:
        return
    fun_a(level+1)
    print(level, end=' ')


fun_a(0)
