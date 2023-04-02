while True:
    d = input()
    if d == '-':
        break
    m = int(input())
    h = [int(input()) for _ in range(m)]
    for i in h:
        d = d[i:] + d[:i]
    print(d)
