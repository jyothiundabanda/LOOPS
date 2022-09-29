i=1
sum=0
while i<=10:
    # user=int(input("enter the number"))
    sum=i+sum
    i+=1
print(sum)





# count
# i=156
# j=157
# while i<=246:
#     if j-i==11:
#         break
#     else:
#         print(j-i)
#     j=j+1


# i=1
# while i<=10:
#     if i==6 or i==8 or i==9:
#         print("*")
#     else:
#         print(i)
#     i+=1



# i=1
# i+=1
# while i<=10:
#     print(i)

# 1 to 10 prime number

# i=1
# while i<=10:
#     j=2
#
#      while j<i:
#         if i%j==0:
#             c=c+1
#         j+=1
#     if c==0:
#         print(i,"prime number")
#     i+=1




from builtins import input


# i=int(input("no"))
# j=int(input("no"))
# c=0
# s=0
# while i<=j:
#     if i%2==0:
#         c=c+i
#     else:
#         s=s+i
#     i+=1
# print(c)
# print(s)



# n=int(input("no"))
# len=len(str(n))
# i=0
# while n>0:
#     i=n%10
#     print(i*i)
#     n=n//10

# n=int(input("no"))
# a=str(n)
# i=0
# c=0
# while i>len(a):
#     r=n%10
#     if r%2==0:
#         i=i+1
#     else:
#         c=c+1
#     n=n//10
# print("evevn",i)
# print("odd",c)


a=1
b=10
while a<=10:
    print(a,b+1)
    a=a+1
    b=b+1