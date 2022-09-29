from builtins import input, int


# n=int(input("no"))
i=0
c=5
while i<=5:
    user=int(input("no"))
    if c<user:
        print("high giuessing")
        print("tyr again")
    elif c>user:
        print("low guessing")
        print("try again")
    elif c==user:
        print("your winner")
        break
    else:
        print(" try again")
    c=c+1
print("tq for playing game")
        