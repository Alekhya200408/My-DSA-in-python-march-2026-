'''
* * * * *
* * * *
* * *
* *
*
'''

def pattern(n):
    for i in range (n+1):
        for j in range(n-i+1):
            print("*",end=" ")
        print()

s=int(input("Enter the number: "))
pattern(s)