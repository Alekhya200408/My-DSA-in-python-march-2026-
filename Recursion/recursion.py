# factorial 

# in loop
# fact =1
# for i in range (1,num+1):
# fact=fact*i

# resursion

n=int(input("Enter a number "))
def fact(n):
    if n==0 or n==1:
        return 1

    return  n * fact(n-1)

print(fact(n))

# Fiibonnaci

f=int(input("Enter a number "))
def fib(f):
    if f==1 or f==2:
        return 1
    return fib(f-1)+fib(f-2)

print (fib(f))