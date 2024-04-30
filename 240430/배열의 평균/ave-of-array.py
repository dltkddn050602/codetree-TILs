arr = []
a = 0
for i in range(2):
    n = input()
    n = n.split()
    for i in range(4):
        n[i] = float(n[i])
    arr.append(n)
for k in range(2):
    a = 0
    for i in range(4):
        a += arr[k][i]
    print("%0.1f" %(a/4), end=" ")
print()

for i in range(4):
    a = arr[0][i] + arr[1][i]
    print("%0.1f" %(a/2), end=" ")
print()

a = 0
for i in range(4):
    a += arr[1][i] + arr[0][i]
print("%0.1f" %(a/8), end=" ")