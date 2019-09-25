k = int(input())
count = {str(i): 0 for i in range(100)}
total = 0

for l_index in range(int(k)):
    a = input().split()
    size = int(a[0])
    total += size
    if size > 0:
        for i in range(1, size +1):
            count[a[i]] += 1
buff = []
for i in range(100):
    c = str(i)
    if i % 10 and buff:
        print(' '.join(buff), end=' ')
        buff = []
    buff.extend([c] * count[c])
print(' '.join(buff))



