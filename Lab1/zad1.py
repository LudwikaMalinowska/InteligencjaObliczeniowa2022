import math


def prime(n):
    n_sqrt = math.sqrt(n)
    # print(n, n_sqrt)
    for i in range(2, math.ceil(n_sqrt)+1):
        # print("i = ", i)
        if n % i == 0:
            # print("n%i", n%i)
            return False

    return True


print(prime(3))
print(prime(4))
print(prime(49))
print(prime(13337))


# ********* 1b


def select_primes(x):
    primes_iterator = filter(prime, x)
    primes_list = list(primes_iterator)

    return primes_list


print("\n****** 1b *******\n")
print(select_primes([3, 6, 11, 25, 19]))
print(select_primes([3,4,5,12,49,113]))

