matriz = [[12, -18, 4, -19, 3, -19, -19],
              [1, 10, 1, -11, 7, -7, 9],
              [-8, -5, -8, -11, 17, 3, -20],
              [13, -18, 9, -6, -14, 3, 20],
              [1, 13, 12, 9, -17, 8, -8],
              [14, -15, 7, -3, 9, 19, 8],
              [14, -4, -3, -14, -18, 12, -12]]
solu = [-6, 6, 3, 5, 4, 5, -11]

n=len(solu)
x=[0 for i in range(n)]
p=[[0]*n for x in range(n)]

def gauss(mat,sol):
    conteo=0
    for i in range(0,n):
        for j in range(i+1,n):
            if mat[j][i]!=0:
                m=mat[j][i]/mat[i][i]
                conteo += 2  # División y asignación
                sol[j]-=m*sol[i]
                conteo += 3  # Multiplicación, sustracción y asignación
                for k in range(i,n):
                    mat[j][k]-=m*mat[i][k]
                    conteo += 3  # Multiplicación, sustracción y asignación
                p[i][j]=m
                conteo += 1  # Asignación

    for i in range(n-1,-1,-1):
        suma=0
        conteo += 1  # Asignación
        for j in range(i+1,n):
            suma+=mat[i][j]*x[j]
            conteo += 3  # Multiplicación, adición y asignación
        x[i]=(sol[i]-suma)/mat[i][i]
        conteo += 3  # Sustracción, división y asignacion
    print(f"Total de operaciones: {conteo}")
    return x

y=[0 for i in range(n)]
y=gauss(matriz,solu)

for i in range(0,n):
    print('x',(i+1),'=',y[i])
