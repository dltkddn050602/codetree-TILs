a = 0
n = input()
n = n.split()
for i in range(3):
    n[i] = int(n[i])

for i in range(3):
    if n[i] > a:
        a = n[i]
    else:
        continue

print(a)