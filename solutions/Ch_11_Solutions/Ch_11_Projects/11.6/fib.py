"""
File: fib.py
Project 11.6

Employs memoization to improve the efficiency of recursive Fibonacci.
"""

def fib(n):
    """Fibonacci function with a table for memoization."""
    table = {}
    
    def memoizedFib(n):
        if n < 3:
            return 1
        else:
            # Attempt to get value for memoizedFib(n)
            # from the table
            # If unsuccessful, recurse and add results to
            # the table
            value = table.get(n, None)
            if value: return value
            else:
                value = memoizedFib(n - 1) + memoizedFib(n - 2)
                table[n] = value
                return value

    return memoizedFib(n)

def main():
    """Tests the function with some powers of 2."""
    problemSize = 2
    print("%4s%12s" % ("n", "fib(n)"))
    for count in range(5):
        print("%4d%12d" % (problemSize, fib(problemSize)))
        problemSize *= 2

if __name__ == "__main__":
    main()

