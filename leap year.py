from builtins import int
from re import S


n=int(input("no"))
i=0
s=0
while n>0:
    if n%4==0:
        i=n-4
        s=i-4
        print(s,i)
    else:
        i=n+4
        s=i+4
        print(s, i)
    break
    