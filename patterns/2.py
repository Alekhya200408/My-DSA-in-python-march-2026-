'''
*
* *
* * *
* * * *
* * * * *
'''

def pattern(n):
    for i in range (n):
        for j in range(i):
            print("*",end=" ")
        print()

s=int(input("Enter the number: "))
pattern(s)
