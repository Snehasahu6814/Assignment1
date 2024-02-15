# Number=int(input("Enter a Number"))
# a=0
# b=1
# if Number<0:
#     print("number is negative")

    
# for i in range(0,Number):
#     print(a,end=" ")
   
#     c=a+b
#     a=b 
#     b=c



def fibonacci(n):
    a=0
    b=1

    if n==1:
        print(a,end=" ")
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c=a+b
            a=b 
            b=c
            print(c,end=" ") 
Number=int(input("Enter a Number "))
print("The fibonacci series of a Number is :")       
fibonacci(Number)           