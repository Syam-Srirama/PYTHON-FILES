n = int(input())
is_prime = True
is_circular_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    num_str = str(n)
    length = len(num_str)
    for i in range(length):
        rotated_num = int(num_str[i:] + num_str[:i])
        for j in range(2, rotated_num):
            if rotated_num % j == 0:
                is_circular_prime = False
                break
        if not is_circular_prime:
            break

if not is_prime:
    print("{} is not a prime number.".format(n))
elif is_prime and not is_circular_prime:
    print("{} is a prime number but not a circular prime.".format(n))
else:
    print("{} is a circular prime.".format(n))
