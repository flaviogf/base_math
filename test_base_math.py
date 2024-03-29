import pytest
from math import sqrt

from base_math import (natural_numbers,
                       pair_numbers,
                       odd_numbers,
                       square_numbers,
                       prime_numbers,
                       is_prime,
                       next_prime,
                       triangular_numbers,
                       integers_number,
                       number_of_integers_in_range)


def test_should_0_1_2_3_4_in_natural_numbers():
    expected = [0, 1, 2, 3, 4]

    result = list(natural_numbers(5))

    assert result == expected


def test_should_0_2_4_6_8_in_pair_numbers():
    expected = [0, 2, 4, 6, 8]

    result = list(pair_numbers(5))

    assert result == expected


def test_should_1_3_5_7_9_in_odd_numbers():
    expected = [1, 3, 5, 7, 9]

    result = list(odd_numbers(5))

    assert result == expected


def test_should_1_4_9_16_25_in_square_numbers():
    expected = [1, 4, 9, 16, 25]

    result = list(square_numbers(5))

    assert result == expected


def test_should_1_3_6_10_15_in_triangular_numbers():
    expected = [1, 3, 6, 10, 15]

    result = list(triangular_numbers(5))

    assert result == expected


def test_should_2_3_5_7_11_in_prime_numbers():
    expected = [2, 3, 5, 7, 11]

    result = list(prime_numbers(5))

    assert result == expected


def test_should_1_2_3_4_5_and_opposite_numbers_in_integers_number():
    expected = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

    result = list(integers_number(5))

    assert result == expected


@pytest.mark.parametrize('x, y', [(1, 2), (4, 5)])
def test_should_next_prime_of_x_equal_to_y(x, y):
    assert next_prime(x) == y


@pytest.mark.parametrize('x', [1, 4, 6, 8, 9])
def test_should_x_not_is_prime(x):
    assert not is_prime(x)


@pytest.mark.parametrize('x', [2, 3, 5, 7, 11])
def test_should_x_is_prime(x):
    assert is_prime(x)


def test_should_number_of_integers_in_range_minus_sqrt_10_and_sqrt15():
    expected = 7

    result = number_of_integers_in_range(-sqrt(10), sqrt(15))

    assert result == expected
