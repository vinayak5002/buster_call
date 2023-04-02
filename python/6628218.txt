while True:
	a, b, c = input().split()
	a = int(a)
	c = int(c)
	if b == "?":
		break
	if b == "+":
		print(a + c)
	if b == "-":
		print(a - c)
	if b == "*":
		print(a * c)
	if b == "/":
		print(a // c)
