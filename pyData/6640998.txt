n = int(input())
line = list(map(int, input().split()))

max = line[0]
min = line[0]
sum = line[0]

for i in range(1, n):
    if max < line[i]:
        max = line[i]
    elif min > line[i]:
        min = line[i]
    sum += line[i]

print(min, max, sum)
