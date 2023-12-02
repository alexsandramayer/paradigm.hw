def calculate_correlation(x, y):
    if len(x) != len(y):
        return "Ошибка: массивы должны иметь одинаковую длину"
    
    n = len(x)  
    sum_x = sum(x)  
    sum_y = sum(y)  
    sum_xy = sum([xi * yi for xi, yi in zip(x, y)])  
    sum_x2 = sum([xi**2 for xi in x])  
    sum_y2 = sum([yi**2 for yi in y])  
    
    
    numerator = n * sum_xy - sum_x * sum_y
    denominator = ((n * sum_x2 - sum_x**2) * (n * sum_y2 - sum_y**2)) ** 0.5
    correlation = numerator / denominator
    
    return correlation


x = [2, 5, 1, 3, 7, 8, 9, 6, 10, 4]
y = [3, 10, 8, 5, 6, 2, 7, 4, 9, 1]
result = calculate_correlation(x, y)
print("Корреляция Пирсона:", result)