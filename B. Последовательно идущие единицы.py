import sys

numbers = sys.stdin.readline().strip()

sumlen = 0
maxlen = 0
for j in range(int(numbers)):
    num = sys.stdin.readline().strip()
    if num == '1':
        sumlen += 1
        maxlen = max(maxlen, sumlen)
    else:
        sumlen = 0
print(maxlen)