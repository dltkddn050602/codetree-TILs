n = input()
n = n.split()
for i in range(3):
    n[i] = int(n[i])
n.sort()

for i in range(n[0],n[2] + 1):
    if i != n[1]:    
        for k in range(1,10):
            print("%d * %d = %d" %(i,k,i*k))
    else:
        continue