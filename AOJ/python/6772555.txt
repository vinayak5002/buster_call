import itertools

while True:
    n, x= map(int, input().split())
    if n == 0 and x == 0:
        break
    else:
        i = list(range(1, n+1))
        count = 0
        for v in itertools.combinations(i, 3):
            v = sum(v)
            if v == x:
                count += 1
        print(count)
        break

