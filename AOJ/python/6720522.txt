from enum import Enum
import sys
import math

BIG_NUM = 2000000000
MOD = 1000000007
EPS = 0.000000001


while True:
    N = int(input())
    if N == 0:
        break
    table = list(map(int,input().split()))

    tmp_sum = 0
    for i in range(len(table)):
        tmp_sum += table[i]
    B = tmp_sum/len(table) #平均

    squared_sum = 0
    for i in range(len(table)):
        squared_sum += table[i]*table[i]
    A = squared_sum/len(table)

    print("%.10f"%(math.sqrt(A-B*B)))
