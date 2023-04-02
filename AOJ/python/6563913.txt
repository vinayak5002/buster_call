while True:
    H, W = map(int, raw_input().split())
    if H == W == 0:
        break
    for i in range(H):
        if W == 1 and i % 2 == 0:
            print "#"
        elif W == 1 and i % 2 == 1:
            print "."
        elif i % 2 == 0:
            print "#." * (W / 2) + "#" * (W%2)
        else:
            print ".#" * (W / 2) + "." * (W%2)
    print

