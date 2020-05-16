#Algoritmo 8 reinas de fuerza bruta, busqueda en profundidad que me recorre todas las posibles soluciones
#sacado de internet

#Estado inicial
#El algoritmo toma como estado inicial varias posiciones , puede iniciar en la a1, a2, a3

#El numero de soluciones son 92.

#Reinas a ubicar
reinas = 8
# nro soluciones que quiero imprimir
solution = 20
#Funcion para validar las reinas
def validarReina(R,reinas):
    for i in range(reinas):     #Ciclo para recorrer las filas
        for j in range(reinas): # recorrer columnas
            if (i != j):
                if(abs(i - j) == abs(R[i] - R[j])):
                    return False
                if (R[i] == R[j]):
                    return False
    return True

def combinatoria(reinas,solution):
    for a in range(reinas):
        for b in range(reinas):
            for c in range(reinas):
                for d in range(reinas):                     #Estos ciclos me van recorriendo todas las casillas validando si
                    for e in range(reinas):                 #se puede colocar la reina o no
                        for f in range(reinas):
                            for g in range(reinas):
                                for h in range(reinas):
                                    v = [a, b, c, d, e, f, g, h]    # Las almacenamos en un vector
                                    validar = validarReina(v,reinas) #Validamos las reinas
                                    if validar == True:
                                        solution = solution - 1    #cuando imprime una solucion, va restando a las indicadas
                                        print v
                                        if solution == 0:
                                            return 0

print combinatoria(reinas, solution)
