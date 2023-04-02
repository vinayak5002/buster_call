
rectangles = []

while True:
    rec = []

    h, w = map(int, input().split())

    if h == w == 0:
        break

    for i in range(h):
        col = ''
        for j in range(w):
            col += '#'
        rec.append(col)

    rectangles.append(rec)

for rec in rectangles:
    for col in rec:
        print(col)
    print('')
