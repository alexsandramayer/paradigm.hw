def sort_list_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

numbers = [6, 4, 3, 5, 9]  
sort_numbers = sort_list_imperative(numbers)
print(sort_numbers)