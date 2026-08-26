def bubble_sort(numbers):
    n=len(numbers)

# in loop of range python does not include the stop values
    for i in range(n-1,0,-1):
        swapped = False

        for j in range(i):
            if(numbers[j]>numbers[j+1]):
                numbers[j],numbers[j+1]=(
                            numbers[j+1],
                            numbers[j]
                        )
                swapped = True
        if not swapped:
            break
    return numbers

values=[9,20,13,26,7,8]

print(bubble_sort(values))

