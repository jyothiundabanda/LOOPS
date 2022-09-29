
# i=int(input("enter the no"))
# a=0
# b=i%10
# while a<b:
#     if b%2==0:
#         print(b,"even")
#         break
#     elif b!=0:
#         print(b,"odd")
#         break
#     i=i+1

from builtins import input
# n=int(input("no"))
# f=1
# while n>0:
#     f=f*n
#     n=n-1
# print(f)

# n=int(input("no"))
# i=n
# while i<n+4:
#     if i%2==0:
#         print(i-4)
        
#     else:
#         print(i+2)
#     i=i+2
    


# floor=int(input("floor"))   
# i=1
# while True:
#     if floor==1:
#         print("101","102","103")
#         room=int(input("enter the room number:"))
#         if room==101:
#             print("1 bed only")
#         elif room==102:
#             print("3 beds only")
#         elif room==103:
#             print("10 beds only")
#         else:
#             print("enter correct room number")
#         break
#     elif floor==2:
#         print("201","202","203","204")
#         room=int(input("no"))
#         if room==201:
#             print("1 bed only")
#         elif room==202:
#             print("3 beds only")
#         elif room==203:
#             print("10 beds only")
#         elif room==204:
#             print("10 beds only")
#         else:
#             print("enter correct room number")
#         break

    
# a="man"
# b=5
# print("man ,"*(b-1)+a)




# a=int(input("no1"))
# b=int(input("no2"))
# symbol=input("symbol")
# if symbol=="+":
#     print(a+b,"addition")
# elif symbol=="-":
#     print(a-b,"substraction")
# elif symbol=="%":
#     print(a%b,"moduls")
# elif symbol=="//":
#     print(a//b,"floor division")
# else:
#     print("ntg")


# i=1
# k=25
# while i<=25:
#     print(i,k+1)
#     i=i+1
#     k=k+1





# i=1
# while i<=3:
#     k=1
#     while k<=5-i:
#         print(" ",end="")
#         k=k+1
#     j=1
#     while j<=i*2-1:
#         print("*",end="")
#         j=j+1
#     i=i+1
#     print()
# i=2
# while i>=1:
#     k=1
#     while k<=5-i:
#         print(" ",end="")
#         k=k+1
#     j=1
#     while j<=i*2-1:
#         print("*",end="")
#         j=j+1
#     i=i-1
    # print()



# # i=1
# # while i<=5:
# #     j=1
# #     while j<=1:
# #         print("*",end="")

# n=int(input("no"))
# i=1
# while i<=n:
#     j=1
#     while j<=i*2-1:
#         print("*",end="")
#         j=j+1
#     i=i+1
#     print()
# i=2
# while i>=1:
#     j=1
#     while j<=i*2-1:
#         print("*",end="")
#         j=j+1
#     i=i-1
#     print()

n=int(input("no"))
i=1
while i<=n:
    j=1
    while j<=i*2-1:
        print("*",end="")
        j=j+1
    i=i+1
    print()
