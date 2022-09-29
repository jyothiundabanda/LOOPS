# n=int(input("enter"))
# a=n
# s=0
# while n>0:
#     s=s+(n%10)*(n%10)*(n%10)
#     n=n//10
# if a==s:
#     print("pri")
# else:
#     print("n")

# n=int(input("no"))
# a=n
# s=0
# len=len(str(n))
# while n>0:
#     r=n%10
#     b=r**len
#     s=s+b
#     n=n//10
# if s==a:
#     print("amstrong number")
# else:
#     print("not")

# n=int(input("no"))
# i=1
# while i<=n:
#     j=1
#     while j<=10:
#         print(i,"*",j,"=",i*j)
#         j=j+1
#     i=i+1
#     print()

# i=10
# while i>=1:
#     print(i)
#     i=i-1

# l="jyojy"
# i=0
# b=[]
# c=0
# while i<len(l)-3:
#     c=l.count(l[i])
#     a=l[i],c
#     b.append(list(a))
#     i=i+1
# print(b)

l=[1,2,3,4,5,6]
j=-1
b=[]
while j<len(l)-1:
    d=[l[j],l[j-1]]
    b.append(d)
    j=j+1
print(b)