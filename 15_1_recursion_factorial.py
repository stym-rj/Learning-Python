# Limit for a recursion call is 1000.

def factorial(n):
    if n<2:
        return 1
    return n*factorial(n-1)

print(factorial(9))