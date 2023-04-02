import sys
s = sys.stdin.read().lower()
a = {chr(i): 0 for i in range(ord('a'), ord('z')+1)}
for i in s:
    if ord(i) in range(ord('a'), ord('z')+1):
        a[i] += 1
[print(f'{k} : {v}') for k, v in a.items()]
