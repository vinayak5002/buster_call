n = int(input())
r_min = int(input())
r_t   = int(input())
g_max = r_t - r_min
r_min = min(r_t,r_min)
for _ in range(n-2):
    r_t = int(input())
    g_max = max(g_max, r_t-r_min)
    r_min = min(r_t,r_min)
print(g_max)
