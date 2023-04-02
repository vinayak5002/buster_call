num=[[[0]*11 for i in range(4)] for j in range(5)]
n=int(input())
for i in range(n):
    b,f,r,v=map(int,input().split())
    num[b][f][r]+=v
for i in range(1,5):
    for j in range(1,4):
        for k in range(1,11):
            print(' ',num[i][j][k],sep='',end='')
        print()
    if i<4:
        for j in range(20):
            print('#',end='')
        print()
