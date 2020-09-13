for i in range(22):
    a = [0]*i
a[0] = 1
for i in range(1,21):
    a[i] = 2*a[i-1]
print(a)