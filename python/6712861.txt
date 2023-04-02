sec = int(input())
h = sec/60/60
m = (sec%3600)//60
s = sec%60
print(f"{int(h)}:{int(m)}:{int(s)}")
