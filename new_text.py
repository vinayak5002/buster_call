from collections import deque
VAR0= int(input())

VAR1= deque()
for LOP0 in range(VAR0) :
    VAR2 = input().split()
    if VAR2[0] == 'insert' :
        VAR1.appendleft(VAR2[1])
    elif VAR2[0] == 'delete' :
        try :
            VAR1.remove(VAR2[1])
        except ValueError :
            pass
    elif VAR2[0] == 'deleteFirst' :
        VAR1.popleft()
    elif VAR2[0] == 'deleteLast' :
        VAR1.pop()
print(*VAR1)

