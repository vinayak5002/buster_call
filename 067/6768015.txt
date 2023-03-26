input_str = input()

for i in input_str:
    if i.islower():
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')
print()
