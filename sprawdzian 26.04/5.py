# def metoda_trapezow(n):

#     def g(x):
#         return -1 * x**2 + 2 * x

#     a = 0
#     b = 2
#     dx = (b - a) / n

#     x = a
#     suma = 0

#     # pola_trapezow = []

#     for i in range(1, n+1):
#         suma += ((g(x) + g(x + dx)) * dx) / 2
#         # pola_trapezow.append(((g(x) + g(x + dx)) * dx) / 2)
#         x += dx
#         # print(f"Pole trapezu {i}: {pola_trapezow[i-1]}")

#     return f"Suma pól trapezów: {suma}"
# print(metoda_trapezow(5))

def metoda_trapez(n):
    def f(x):
        return -1 * x**2 + 2 * x
    
    a = 0
    b = 2
    dx = (b-a)/n
    x = a 
    suma = 0
    for i in range(1, n + 1):
        suma += ((f(x) + f(x + dx)) * dx) / 2
        x += dx
    return suma

print(metoda_trapez(5))