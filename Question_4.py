#Question 4

def recursiveFunction(n):
    if n >= 0:
        print(n)
        n-=1
        recursiveFunction(n)
    
recursiveFunction(50)
