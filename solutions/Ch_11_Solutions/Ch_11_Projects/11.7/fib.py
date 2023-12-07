"""
File: fib.py
Project 11.7

Employs memoization to improve the efficiency of recursive Fibonacci.
Counts the calls and displays the results.
"""

class Counter(object):
    """Tracks a count."""

    def __init__(self):
        self._number = 0

    def increment(self):
        self._number += 1

    def __str__(self):
        return str(self._number)

def fib(n, counter = None):
    """Fibonacci function with a table for memoization."""
    table = {}
    
    def memoizedFib(n):
        if counter: counter.increment()
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
    print("%12s%15s" % ("Problem Size", "Calls"))
    for count in range(5):
        counter = Counter()

        # The start of the algorithm (note the empty dictionary)
        fib(problemSize, counter)
        # The end of the algorithm
    
        print("%12d%15s" % (problemSize, counter))
        problemSize *= 2

if __name__ == "__main__":
    main()

