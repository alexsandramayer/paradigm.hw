def binary_search(arr, target):
    def binary_search_recursive(left, right):
        if left > right:
            return -1
        
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return binary_search_recursive(mid + 1, right)
        else:
            return binary_search_recursive(left, mid - 1)
    
    return binary_search_recursive(0, len(arr) - 1)

# Пример использования
array = [1, 3, 5, 7, 9, 11, 15]
target = 15

print(f"Исходный массив: {array}")

result = binary_search(array, target)
if result != -1:
    print("Искомый элемент найден на позиции", result)
else:
    print("Искомый элемент не найден")
