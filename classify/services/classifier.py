"""service file for number classification"""

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_perfect(n):
    """Check if a number is perfect (sum of proper divisors equals the number)."""
    if n < 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n


def is_armstrong(n):
    """Check if a number is an Armstrong number."""
    if n < 0:
        return False
    num_str = str(n)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == n


def is_even(n):
    """Check if a number is even."""
    return n % 2 == 0


def classify_number(n):
    """Classify a number based on its properties."""
    return {
        "number": n,
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "is_armstrong": is_armstrong(n),
        "is_even": is_even(n),
        "is_odd": not is_even(n),
    }

