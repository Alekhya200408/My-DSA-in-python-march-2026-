def insertion_sort(numbers):
    n=len(numbers)

    for i in range(n):
        j=i
        while(j>0 and numbers[j-1]>numbers[j]):
            numbers[j-1],numbers[j]=(
                numbers[j],
                numbers[j-1]
            )
            j=j-1
    return numbers

values=[9,12,14,15,6,8,13]

print(insertion_sort(values))