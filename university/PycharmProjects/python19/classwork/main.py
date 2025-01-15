import time

row = int(input('Row: '))
col = int(input('Column: '))

# row - qator
# col - ustun
midRow = row // 2 + 1
midCol = col // 2 + 1
for i in range(1, row + 1):
    # print('0', end=' ')
    for j in range(1, col + 1):
        # if (j == 1 or i == 1 or j == col
        #     or i == row or i == midRow
        #     or j == midCol
        # ):
        # if j == i:
        # if i >= j:
        #     print('0', end=' ')
        # else :
        #     print('*', end=' ')
        # time.sleep(0.2)
        if j != col:
            print(j, end=' ')
        else:
            print(i, end=' ')
    print()