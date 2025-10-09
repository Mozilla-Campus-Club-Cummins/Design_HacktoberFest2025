x, y = 2, 7  # define the range [x, y]

# create a boolean list to mark primes, assume all are prime initially
primes = [True] * (y + 1)

# 0 and 1 are not prime
primes[0], primes[1] = False, False

# Sieve of Eratosthenes to mark non-primes
for i in range(2, int(y ** 0.5) + 1):
    if primes[i]:
        for j in range(i * i, y + 1, i):
            primes[j] = False

# collect primes in the range [x, y]
res = [i for i in range(x, y + 1) if primes[i]]
print(res if res else "No")
