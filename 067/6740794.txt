while True:
	n, p = map(int, input().split())
	if n == 0: break
	ans, m = 0, p
	x = [0]*53
	while True:
		m -= 1
		if m >= 0:
			x[ans] += 1
			if x[ans] == p: break
		else: m = x[ans]; x[ans] = 0
		ans += 1
		if ans == n: ans = 0
	print(ans)
