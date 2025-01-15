# 1
# lastName = input('Enter your lastName: ')
# def malOrFemale(name):
#     if name[-1] == 'a':
#         return 'ayol'
#     else:
#         return 'erkak'

# result = malOrFemale(lastName)
# print(result)

# 2
# def number(a):
#     if 100 <= abs(a) <= 999:
#         return True
#     else:
#         return False
# a = int(input('Enter a number: '))
# print(number(a))


# 3
# def teskarigaOgirish(text):
#     # text2 = ''
#     # for i in text:
#     #     text2 = i + text2
#     # return text2
#     # return text[::-1]
#     i = len(text) - 1
#     b = ''
#     while i >= 0:
#         b += text[i]
#         i -= 1
#     return b
# text = input('text: ')
# print(teskarigaOgirish(text))

# 4
def slicing(text):
    start = int(input('start: '))
    finish = int(input('finish: '))
    a = ''
    if start < finish:
        for letter in range(start, finish + 1):
            a += text[letter]
            print(text[letter])
        return a
    else: return 'ERROR!'

text = input('text: ')
print(slicing(text))





    