# Primes

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def primes_minor_than(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

# Example usage
n = 6  # Change this value to generate a different number of primes
prime_numbers = primes_minor_than(n)
print(prime_numbers)  # Output: [2, 3, 5]

def first_nth_primes(n):
    primes = []
    is_prime = [True] * (n * 10)  # Use a larger size for the sieve array to accommodate more primes
    
    num = 2
    while len(primes) < n:
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, len(is_prime), num):
                is_prime[multiple] = False
        num += 1
    
    return primes

# Example usage
n = 10  # Change this value to generate a different number of primes
prime_numbers = first_nth_primes(n)
print(prime_numbers)  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]