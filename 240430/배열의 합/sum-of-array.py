arr = []

for i in range(4):
    n = input()
    n = n.split()
    for i in range(4):
        n[i] = int(n[i])
    arr.append(n)

for i in range(4):
    sum = 0
    for k in range(4):
        sum += arr[i][k]
    print(sum)