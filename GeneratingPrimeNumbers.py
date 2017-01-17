
def prime_generator(n):
    # raise ValueError is n is less than two
    if n < 2:
        raise ValueError("number is less than two")
    primes = []
    for num in range(2, n+1):
        prime = True
        for x in range(2, int(num/2)+1):
            if num % x == 0:
                prime = False
        if prime is True:
            primes.append(num)

    return primes
