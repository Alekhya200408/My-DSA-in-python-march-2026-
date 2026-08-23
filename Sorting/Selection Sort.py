def selection_sort(numbers):
    n=len(numbers)

    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if numbers[j]<numbers[min]:
                min=j
        numbers[i],numbers[min]=(
            numbers[min],
            numbers[i]
        )
    return numbers

values=[13,46,24,52,20,9]

print(selection_sort(values))