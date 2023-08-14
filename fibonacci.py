def fibonacci_series(n):
    series = [0, 1]  # Initializing the first two numbers in the series
    while len(series) < n:
        next_num = series[-1] + series[-2]
        series.append(next_num)
    return series

# Generating the first 10 numbers in the Fibonacci series
n = 20
fib_series = fibonacci_series(n)
print(f"Fibonacci Series (first {n} numbers):", fib_series)
