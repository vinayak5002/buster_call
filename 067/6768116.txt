s = input()
n = int(input())
orders = [input().split() for _ in range(n)]
for order in orders:
    a, b = map(int, order[1:3])
    if order[0] == 'print':
        print(s[a:b+1])
    elif order[0] == 'replace':
        s = s[0:a] + order[3] + s[b+1:]
    elif order[0] == 'reverse':
        s = s[0:a] + s[a:b+1][::-1] + s[b + 1:]
