# ****
# ****
# ****
# ****
# n x n pattern

def four_star(n):
    for i in range(n):
        for j in range(n):
            print("*",end=' ')
        print()

four_star(2)