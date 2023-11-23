import numpy as np


# Función para calcular el determinante de una matriz

def determinante(mat):
    return np.linalg.det(mat)


def cramer(matriz, solu):
    copia = matriz.copy()
    det = np.linalg.det(matriz)
    dets = np.array([])
    if det != 0:
        for i in range(7):
            for j in range(7):
                copia[j][i] = solu[j]
            dets = np.append(dets, (determinante(copia)) / det)
            copia = matriz.copy()
        for i in range(7):
            print("x", i + 1, " es ", dets[i])
    else:
        print("El sistema no tiene solucion")


m = np.array([[12, -18, 4, -19, 3, -19, -19],
              [1, 10, 1, -11, 7, -7, 9],
              [-8, -5, -8, -11, 17, 3, -20],
              [13, -18, 9, -6, -14, 3, 20],
              [1, 13, 12, 9, -17, 8, -8],
              [14, -15, 7, -3, 9, 19, 8],
              [14, -4, -3, -14, -18, 12, -12]])
s = np.array([-6, 6, 3, 5, 4, 5, -11])

cramer(m, s)
