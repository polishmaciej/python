# def szukanie_miejsca_zerowego_bisekcja(eps):

#     def f(x):
#         return x ** 2 - 60

#     a = 1
#     b = 10
#     # i = 1

#     while abs(b - a) > eps:
#         c = (a + b) / 2
#         if f(c) > 0:
#             b = c
#             # print(f"krok {i}: miejsce zerowe w przedziale [{a};{b}]")
#             # i += 1
#         else:
#             a = c
#             # print(f"krok {i}: miejsce zerowe jest w przedziale [{a};{b}]")
#             # i += 1

#     return f"Miejsce zerowe funkcji znajduje się dla x = {round(a, 3)}"

def miejsce_zerowe(eps):
    def f(x):
        return x ** 2 - 60

    a = 1
    b = 10

    while abs(b-a) > eps:
        c = (a+b) / 2
        if f(c) > 0:
            b = c
        else:
            a = c 
          
    return (a+b) / 2

print(miejsce_zerowe(0.001))



