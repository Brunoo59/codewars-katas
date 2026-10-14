def roots(a,b,c):
    
    discriminante = b**2 - 4 * a * c
    
    if discriminante < 0:
        return None
    
    solucion1 = (-b + discriminante**0.5) / (2 * a)
    solucion2 = (-b - discriminante**0.5) / (2 * a)
    
    suma = solucion1 + solucion2 
    
    return round(suma, 2)