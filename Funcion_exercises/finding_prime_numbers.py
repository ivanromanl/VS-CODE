"""Find the prime numbers in a list."""


def is_prime(number):
    """Return True if the number is prime."""
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

def find_primes(numbers):
    """Return a list containing only prime numbers."""
    prime_numbers =[]

    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)

    return prime_numbers

result = find_primes([1, 4, 6, 7, 13, 9, 67])
print(result)
