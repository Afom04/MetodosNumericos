import math

#Método de la serie sin raíz(Leibniz y Gregori)


n = 1
res = 0
for i in range (1000):
    res+=((-1)**(n+1))/(2*(n)-1)
    n+=1

res *=4;

error=math.pi-res

print ("El valor de la serie de Leibniz y Gregori es: ",res)
print("El error absoluto en esta aproximacion es: ", error)