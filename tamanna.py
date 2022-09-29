from builtins import input


# n=int(input("no"))
# i=1
# while n>0:
#     j=1
#     while j<i:
#         print(" ",end="")
#         j=j+1
#     b=1
#     while b<=n:
#         print("*",end=" ")
#         b=b+1
#     i=i+1
#     print()
#     n=n-1

n=int(input("no"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    i=i+1
    print()
m=4
a=2
while a>=1:
    print(str(m)*a," ")
    m=m+1
    a=a-1


# n=int(input("no"))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(j,end="")
#         j=j+1
#     print()
#     k=1
#     while k<=i:
#         print("*",end="")
#         k=k+1
#     i=i+1
#     print()


# n=int(input("no"))
# i=5
# while i>=n:
#     j=1
#     while j<=i:
#         print(" ",end=" ")
#         j=j+1
#     b=1
#     while b<=i:
#         print("*",end=" ")
#         b=b+1
#     i=i+1
#     print()


# n=int(input("no"))
# i=5
# while i>=1:
#     k=0
#     while k<n-i:
#         print(" ",end="")
#         k=k+1
#     a=0
#     while a<i:
#         print("*",end=" ")
#         a=a+1
#     i=i-1
#     print()

# a=int(input("no"))
# n=int(input("no2"))
# i=1
# s=0
# # c=0
# while i<n:
#     s=s+i
#     # c=c+i
#     i=i+1
# print(s)

# # a=8
# b="mango"
# c="man"
# d=a*a
# e=d-a
# f=str(e)
# print(f+b+c)

# a=3
# b="likki"
# c="sai"
# d=a*a
# e=d*a
# f=e-1
# g=d*d
# # print(f,"-",a,"=",g,"("+"#"+",""#"+",""#"+")",",""(@)")

# # print("(""#"+"#"+"#","+","#"+"#"+"#","+","#"+"#"+"#",",",b,")")
# print("("+"###","+","###","+","###",b+")")




# i=1
# while True:
#     room=int(input("enter the room"))
#     if room==101:
#         print("1 bed ")
#         break
#     elif room==102:
#         print("3 beds ")
#         break
#     elif room==303:
#         print("8 beds ")
#         break
#     elif room==201 or room==302:
#         print("no beds ")
#         break
#     elif room==103 or room==202 or room==203 or room==204 or room==301 or room==304 or room==401 or room==402 or room==403 or room==404:
#         print("10 beds ")
#         break
#     else:
#         print("enter correct room no")
#     i=i+1