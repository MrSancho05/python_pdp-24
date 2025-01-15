import random
import string

# TASK 1 KO'CHIRDIM
rows = int(input("rows: "))
cols = int(input("cols: "))

# for i in range(rows):
#     for j in range(cols):
#         random_char = random.choice(string.ascii_uppercase)
#         print(random_char, end='')
#     print()

# TASK 2 NICE
# for i in range(1, rows + 1):
#     for j in range(1, cols + 1):
#         if i == j or i + j == rows + 1 or i == 1 or i == rows:
#             print(i, end=" ")
#
#         else:
#             print(' ', end=" ")
#     print()


# TASK 3 KO'CHIRDIM
# for i in range(1, rows+1):
#     for j in range(1, cols + 1):
#         if i + j == cols + 1 or i == j or j == rows or j == 1:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# TASK 4 KO'CHIRDIM:(
# sanoq = 0
# for i  in range(rows):
#     for j in range(cols):
#         sanoq += 1
#         if i == j or i + j == cols - 1 or j == rows - 1 or j == 0:
#             # print('0', end=' ')
#             print(f"{sanoq:02} ", end='')
#         else:
#             print('  ', end=' ')
#     print()

# TASK 5
# for i in range(rows):
#     for j in range(cols):
#         if i == j or i + j == cols - 1 or i == 0 or i == cols - 1 or j == 0 or j == rows - 1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# TOLISHI KERAK EKAN
for i in range(rows):
    for j in range(cols):
        if (i == j or i + j == cols - 1 or i == 0
                or i == cols - 1 or j == 0
                or j == rows - 1):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()
