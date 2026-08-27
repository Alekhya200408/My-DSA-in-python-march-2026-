'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

def pattern(n):
    for i in range (2*n):
        stars=i
        if(i>n):
            stars=2*n-i
        for j in range(stars):
            print("*",end=" ")
        print()

s=int(input("Enter the number: "))
pattern(s)

