def fibonacci(n):
    current = 0
    next = 1
    
    for i in range(n):
        print(current)
        tmp = current
        current = next
        next = next + tmp

# Voglio rendere questo modulo utilizzabile come script lanciabile da console
# tramite comando "python fibonacci.py 10"
if __name__ == "__main__":
    import sys
    fibonacci(int(sys.argv[1]))