J = input()
S = input()
sumcnt = 0
newJ = []
for j in J:
    if j not in newJ: newJ.append(j)
for s in S:
    if s in newJ:
        sumcnt += 1
print(sumcnt)
