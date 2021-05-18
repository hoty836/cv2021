import sys
input = sys.stdin.readline

n = int(input())
stack = []
result = ''
start = 0
flag = True

for i in range(n):
    a=int(input())

    if start < a:
        for k in range(start, a):
            stack.append(k+1)
            result += '+\n'
        start = a
    elif a!= stack[-1]:
        flag = False

    stack.pop()
    result += '-\n'

if flag:
    print(result)
else :
    print('NO')
