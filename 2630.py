n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
blue, white = 0,0 #blue, white count

def square(x, y, n):
    global matrix, blue, white
    check = True
    first_color = matrix[x][y]

    for i in range(x, x+n):
        if not check: break

        for j in range(y, y+n):
            if matrix[i][j] != first_color:
                check = False
                k = n//2
                square(x, y, k)
                square(x+k, y, k)
                square(x, y+k, k)
                square(x+k, y+k, k)
                break

    if check:
        if first_color == 1:
            blue += 1
            return
        elif first_color == 0:
            white += 1
            return


square(0, 0, n)
print(f'{white}\n{blue}')
