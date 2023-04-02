import math
a,b,C=map(float,input().split())
θ=math.radians(C)
h=b*math.sin(θ)
S=(a*h)/2
c=math.sqrt(a**2+b**2-2*a*b*math.cos(θ))
L=a+b+c
print(S,L,h,sep="\n")
