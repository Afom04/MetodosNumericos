import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(np.sin(x))-x**2
x = np.arange(-5, 5, 0.1)

plt.plot(x,f(x))
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.show()

######################
# segunda prueba

# Puntos a tomar
a = -2
b = 0
# Suma
c = b + a
n = 100 # iteraciones
ed = pow(10,-12) # Error deseado
e = 1  # Siempre debe ser e > 1

# Siguiendo las diapositivas

if( f(a) * f(b) < 0):
    i = 0
    while( i <= n and e > ed and f(c) != 0):
        ca = c # valor anterior
        c = (b + a)/2  # Encontrar el punto medio
        # Saber que intervalo nos sirve
        if( f(a) * f(c) < 0 ):
            b = c
        else:
            a = c
            #Calcular el error
        e = abs( (c - ca)/c )*100
        i += 1
    print('La raiz es:',c,'- Error: ',e,' Iteración', i)
else:
    print('El intervalo no es válido')


# cambio de funcion, mismo codigo
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**5-3*x**4+5*x-10
x = np.arange(0,4, 0.1)

plt.plot(x,f(x))
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.show()

######################

# Puntos a tomar
a = -2
b = 1
# Suma
c = b + a
n = 100 # iteraciones
ed = pow(10,-12) # Error deseado
e = 1  # Siempre debe ser e > 1

# Siguiendo las diapositivas

if( f(a) * f(b) < 0):
    i = 0
    while( i <= n and e > ed and f(c) != 0):
        ca = c # valor anterior
        c = (b + a)/2  # Encontrar el punto medio
        # Saber que intervalo nos sirve
        if( f(a) * f(c) < 0 ):
            b = c
        else:
            a = c
        #Calcular el error
        e = abs( (c - ca)/c )*100
        i += 1
    print('La raiz es:',c,'- Error: ',e,' Iteración', i)
    print(f(c))
else:
    print('El intervalo no es válido')


###########################

import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**5-3*x**4+5*x-10*x
x = np.arange(-2,3.5, 0.1)

plt.plot(x,f(x))
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.show()

######

# Puntos a tomar
a = 2
b = 4
# Suma
c = b + a
n = 100 # iteraciones
ed = pow(10,-12) # Error deseado
e = 1  # Siempre debe ser e > 1

if( f(a) * f(b) < 0):
    i = 0
    while( i <= n and e > ed and f(c) != 0):
        ca = c # valor anterior
        c = (b + a)/2  # Encontrar el punto medio
        # Saber que intervalo nos sirve
        if( f(a) * f(c) < 0 ):
            b = c
        else:
            a = c
        #Calcular el error
        e = abs( (c - ca)/c )*100
        i += 1
    print('La raiz es:',c,'- Error: ',e,' Iteración', i)
    print(f(c))
else:
    print('El intervalo no es válido')



