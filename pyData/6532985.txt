R_min, dR_max = float("inf"), -float("inf")
for _ in range(int(input())):
    R = int(input())
    dR_max = max(dR_max, R-R_min)
    R_min = min(R_min, R)
print(dR_max)
