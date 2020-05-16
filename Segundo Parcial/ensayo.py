filas_columnas = 8

def evaluacion(col, reinas):
    izquierda = derecha = col

    for r, c in reversed(reinas):
        izquierda, derecha = izquierda - 1, derecha + 1

        if c in (izquierda, col, derecha):
            return True
    return False

def resolver(n):
    if n == 0:
        return [[]]

    solucion_c = resolver(n - 1)

    return [solucion+[(n,i+1)]
        for i in xrange(filas_columnas)
            for solucion in solucion_c
                if not evaluacion(i+1, solucion)]
for respuesta in resolver(filas_columnas):
    print respuesta
