num = int(input("Enter a number: "))
a, b = 0, 1
while b < num:
    a, b = b, a + b
if abs(a - num) < abs(b - num):
    nearest_fib = a
else:
    nearest_fib = b
print(f"The nearest Fibonacci number to {num} is {nearest_fib}.")
