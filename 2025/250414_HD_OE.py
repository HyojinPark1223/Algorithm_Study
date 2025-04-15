N = int(input())

def func(num, result):
    if num == N:
        return result + num

    return func(num + 2, result + num)

if N % 2 == 0:
    print(func(2, 0))
else:
    print(func(1, 0))