import pytest

from base_math import (natural_numbers,
                       pair_numbers,
                       odd_numbers,
                       square_numbers,
                       prime_numbers,
                       is_prime,
                       next_prime)


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


def test_should_2_3_5_7_11_in_prime_numbers():
    expected = [2, 3, 5, 7, 11]

    result = list(prime_numbers(5))

    assert result == expected


@pytest.mark.parametrize('x, y', [(1, 2), (4, 5)])
def test_should_next_prime_of_x_equal_to_y(x, y):
    assert next_prime(x) == y


@pytest.mark.parametrize('number', [1, 4, 6, 8, 9])
def test_should_not_is_prime(number):
    assert not is_prime(number)


@pytest.mark.parametrize('number', [2, 3, 5, 7, 11])
def test_should_11_is_prime(number):
    assert is_prime(number)
