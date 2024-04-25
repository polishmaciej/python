# def metoda_prostokatow(n):

#     def h(x):
#         return -1 * x**2 + 2 * x

#     a = 0
#     b = 2
#     dx = (b - a) / n

#     x = a
#     suma = 0

#     # Pola_prostokatow = []
#     for i in range(1, n+1):
#         suma += dx * h(x + dx)
#         # Pola_prostokatow.append(dx * h(x + dx))
#         # print(f"Pole prostokątu {i}: {Pola_prostokatow[i-1]}")
#         x += dx

#     return "Suma pól prostokątów " + str(suma)

# print(metoda_prostokatow(5))


def metoda_prostokatow(n):

    def funkcja(x):
       return -1*x**2+2*x
    

    suma = 0
    a = 0
    b = 2
    x = a
    dx = (b-a) / n

    for i in range(1, n + 1):
        suma += dx * funkcja(x + dx)
        x += dx

    return suma
    
print(metoda_prostokatow(5))
