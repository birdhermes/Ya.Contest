
import sys


n = int(input())
dlina = []
current = 0
for i in range(n):

    a = sys.stdin.readline().strip()
    if a != current:
        dlina.append(a)
    current = a
for i in dlina:
    print(i)