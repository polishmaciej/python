# szukanie pierwiastka z x metodą newtona raphsona
def newton_raphson(x):
    a = 1
    b = 3
    eps = 0.0001
   
    print(f"Początkowe wartosci: a = {a}, b = {b}")
    while abs(b - a) > eps:
        Pole = a * b
        a = (a + b) / 2
        b = Pole / a

    return f"Pierwiastek z {x} = {round(a, 3)}"

