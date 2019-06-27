from math import ceil, floor


def natural_numbers(quantity):
    for it in range(quantity):
        yield it


def pair_numbers(quantity):
    for it in range(0, quantity * 2, 2):
        yield it


def odd_numbers(quantity):
    for it in range(1, quantity * 2, 2):
        yield it


def square_numbers(quantity):
    for it in range(1, quantity + 1):
        yield it ** 2


def prime_numbers(quantity):
    current = 2

    primes = set()

    while len(primes) < quantity:
        current = current if is_prime(current) else next_prime(current)
        primes.add(current)
        current += 1

    for it in primes:
        yield it


def triangular_numbers(quantity):
    for it in range(1, quantity + 1):
        yield sum(range(1, it + 1))


def integers_number(quantity):
    for it in range(-quantity, quantity + 1):
        yield it


def next_prime(n):
    return n if is_prime(n) else next_prime(n + 1)


def is_prime(n):
    dividers_of_n = [it for it in range(1, n + 1) if n % it == 0]
    return len(dividers_of_n) == 2


def number_of_integers_in_range(start, stop):
    return len({it for it in range(round(start), round(stop))})
