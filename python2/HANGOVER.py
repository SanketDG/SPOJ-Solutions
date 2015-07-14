p = [0]
for i in range(1, 277):
    p.append(p[i - 1] + 1. / (i + 1))

n = float(input())

while n != 0.00:
    r = 0
    while p[r] < n:
        r += 1
    print "%d card(s)" %r
    n = float(input())