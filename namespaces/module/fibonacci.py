def fibonacci(n):
    current = 0
    next = 1
    
    for i in range(n):
        print(current)
        tmp = current
        current = next
        next = next + tmp
