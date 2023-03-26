while True:
    str_n=input()
    if str_n=="0":
        break
    list_n=list(str_n)
    ans=0
    for n in list_n:
        ans+=int(n)
    print(ans)
