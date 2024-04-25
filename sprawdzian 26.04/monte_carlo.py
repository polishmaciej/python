def metoda_monte_carlo_pi(n):
    from random import uniform
    # n - liczba punktów w kwadracie
    # n0 - liczba punktów w kole

    # pi * r**2  / a**2  == n0 / n
    # pi * r**2  / 4r**2 == n0 / n
    # pi / 4 == n0 / n
    # pi == 4 * n0 / n
    n0 = 0
    for i in range(n-1):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x * x + y * y <= 1:
            n0 += 1

    pi = 4 * n0 / n
    return pi

print(metoda_monte_carlo_pi(1000000))
