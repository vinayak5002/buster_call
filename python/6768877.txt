while True:
    cards=input()
    if cards=="-":
        break
    m=int(input())
    for i in range(m):
        sh=int(input())
        former=cards[:sh]
        later=cards[sh:]
        cards=later+former
    print(cards)
