# dayName = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# for week in range(1,5):
#     print(f'Week : {week}')
#     for day in dayName:
#         print(f'\t{day}')

# TUSHUNMADIM

# for num in range(1, 1000):
#     for i in range(len(str(num)) // 2):
#         if str(num)[i] != str(num)[-i-1]:
#             break
#     else:
#         print(num)

# list = range(1, 1001)
#
# for i in list:
#     if str(i)[]


# for i in range(1,6):
#     for j in range(1,6):
#         print('*', end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j == 1 or i == 1 or i == 5 or j == 5:
#             print('0', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# new task
row = int(input("Enter row: "))
col = int(input("Enter col: "))
#
# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (i == 1 or j == 1
#                 or i == row
#                 or j == col):
#             print("0", end=" ")
#         else: print(" ", end=" ")
#     print()


# NEW TASK
# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if i == j:
#             print("*", end=" ")
#         else: print(" ", end=" ")
#     print()

# NEW TASK
mid = col // 2
# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if col % 2 != 0:
#             if (i == 1 or j == 1
#                     or i == row
#                     or j == col or j == mid + 1):
#                 print("0", end=" ")
#             else: print(" ", end=" ")
#         else:
#             if (i == 1 or j == 1
#                     or i == row
#                     or j == col or j == mid + 1 or j == mid):
#                 print("0", end=" ")
#             else: print(" ", end=" ")
#     print()

# new task
print(mid)
midRow = row // 2 + 1
for i in range(1, row + 1):
    for j in range(1, col + 1):
        if i == 1 or j == mid + 1 or j == 1 and i < midRow or j == col and i < midRow:
            print("*", end=" ")
        else:
            print(' ', end=' ')
    print()