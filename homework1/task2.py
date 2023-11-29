def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers = [6, 4, 3, 5, 9]  
sort_numbers = sort_list_declarative(numbers)
print(sort_numbers)