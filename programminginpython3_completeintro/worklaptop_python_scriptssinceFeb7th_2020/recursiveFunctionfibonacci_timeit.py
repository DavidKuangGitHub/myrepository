'''recursiveFunctionfibonacci_timeit.py'''
import timeit

def fibonacci(n):
    if(n == 0):
        result = 0
    elif(n == 1):
        result = 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

if __name__ == '__main__':
    import timeit
    t1 = timeit.Timer("fibonacci(20)", "from __main__ import fibonacci")
    print("fibonacci ran:",t1.timeit(number=1000), "milliseconds")
