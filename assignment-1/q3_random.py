"""Q3 - Random numbers"""

import random
from collections import Counter

roll_no = 1024170242
random.seed(roll_no)

numbers = [random.randint(100, 900) for _ in range(100)]
print("numbers:", numbers)

odd = [n for n in numbers if n % 2 != 0]
even = [n for n in numbers if n % 2 == 0]
print("odd count:", len(odd))
print("odd numbers:", odd)
print("even count:", len(even))
print("even numbers:", even)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [n for n in numbers if is_prime(n)]
print("prime count:", len(primes))
print("prime numbers:", primes)

number, times = Counter(numbers).most_common(1)[0]
print("most frequent number:", number, "occurring", times, "times")
