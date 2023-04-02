n = int(input())
cards = [input().split() for _ in range(n)]
p_t = 0
p_h = 0
for card in cards:
    if card[0] == card[1]:
        p_t += 1
        p_h += 1
    elif card[0] > card[1]:
        p_t += 3
    else:
        p_h += 3
print(p_t, p_h)
