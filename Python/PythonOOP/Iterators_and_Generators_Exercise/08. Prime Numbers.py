def is_prime(num):
    if num == 0 or num == 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False

    return True


def get_primes(seq):
    primes = filter(lambda n: is_prime(n), seq)
    for num in primes:
        yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
