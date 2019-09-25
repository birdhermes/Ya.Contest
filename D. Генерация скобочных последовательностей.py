import sys
n = int(sys.stdin.readline().strip())

def skobki(current, left, right, pairs):
    if left == pairs and right == pairs:
        print(current)
    else:
        if left < pairs:
            skobki(current + '(', left + 1, right, pairs)
        if right < left:
            skobki(current + ')', left, right + 1, pairs)



skobki('', 0, 0, n)