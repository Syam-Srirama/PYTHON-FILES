# Input numbers
num1 = int(input())
num2 = int(input())

# Find the greatest common divisor (GCD)
a, b = num1, num2
while b:
    a, b = b, a % b
gcd = a

# Calculate the LCM using the formula: LCM(a, b) = abs(a*b) // gcd(a, b)
lcm = abs(num1 * num2) // gcd

print("The LCM of", num1, "and", num2, "is", lcm)
