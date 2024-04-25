def pierwiastek_z_x_bisekcja(x):
    a = 1
    b = x
    eps = 0.0001
  
    while abs(b - a) > eps:
        pierwiastek = (a + b) / 2
        if pierwiastek * pierwiastek > x:
            b = pierwiastek
        
        else:
            a = pierwiastek


    return f"pierwiastek z {x} = {round(a, 3)}"


print(pierwiastek_z_x_bisekcja(16))