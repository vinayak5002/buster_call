while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    op = str(op)
    if op == "?":
        break
    elif op == "+":
        print(int(a + b))
    elif op == "-":
        print(int(a - b))
    elif op == "*":
        print(int(a * b))
    elif op == "/":
        print(int(a / b))
    else:
        pass
