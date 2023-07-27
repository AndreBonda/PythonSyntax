def fibonacci_recursive(n):
    if n == 0:
        return 0
    
    if n == 1:
        return 1

    result = fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    print(result)
    return result