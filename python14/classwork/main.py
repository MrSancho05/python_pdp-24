x = [1,2,3,36,2,1,0,-1,-5]

max = x[0]
maxI = 0
x2 = []
i = 0
while i < len(x):
    if max < x[i] : 
        max = x[i]
        maxI = i
    if max > x[maxI + 1]:
        x2 = x[maxI + 1: len(x)]
    i += 1

print(x2)

i2 = 0
sanoq = 0
while i2 < len(x2):
    if x2[i2] > x2[[i2] + 1]:
        sanoq += 1
    i2 += 1
print(sanoq)
