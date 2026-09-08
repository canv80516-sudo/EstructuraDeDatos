def factorial(n): 
    if n == 0: 
        return 1
    else: 
        return n*factorial(n-1)
a= 10
print(factorial(a)) 