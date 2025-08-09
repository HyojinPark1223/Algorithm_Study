# 25.08.09 백준 10828 STACK
# 쉽다고 생각했는데 계속 시간초과남..
# 한 줄을 받을 때는 input을 사용해도 되지만, 반복문을 통해 입력받을 때는 input함수 사용 시 런타임 에러가 난다.
#* 입출력 속도 비교 : sys.stdin.readline > raw_input() > input()

import sys
sys.stdin = open("input.txt", 'r')

n = int(sys.stdin.readline())

stack = []
for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        stack.append(command[1])

    elif command[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif command[0] == 'size':
        print(len(stack))

    elif command[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack) - 1])