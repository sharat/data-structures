### Author: Sarath
import timeit

### Optimization of Fibonacci sequence using Dynamic Programming
def fib_normal(n = 10):
    if n == 0 or n == 1:
        return 1
    
    return n+fib_normal(n-1)

def fib_dp(n = 10, m = {0:1, 1:1}):

    if not n in m:
        m[n] = fib_dp(n-1,m) +  fib_dp(n-2,m)
    return m[n]

def fib_dpbottomup(n = 10):

    if n == 0:
        return 0
    else:
        prevFib = 1
        currentFib = 1
        newFib = 0
        for x in range(n-1, 0, -1):
            newFib = prevFib + currentFib
            prevFib = currentFib
            currentFib = newFib
        return currentFib 


def testFactorial():

    print 'optimized'
    print(timeit.timeit("fib_dp(25)", setup="from __main__ import fib_dp")) 
    print(timeit.timeit("fib_dp(10)", setup="from __main__ import fib_dp"))


    print 'optimized bottom up'
    print(timeit.timeit("fib_dpbottomup(25)", setup="from __main__ import fib_dpbottomup")) 
    print(timeit.timeit("fib_dpbottomup(10)", setup="from __main__ import fib_dpbottomup"))
    
    print 'Normal'
    print(timeit.timeit("fib_normal(25)", setup="from __main__ import fib_normal")) 
    print(timeit.timeit("fib_normal(10)", setup="from __main__ import fib_normal"))

### End Fibonacci series


def main():
    testFactorial();


    
if __name__ == '__main__':
    main()
