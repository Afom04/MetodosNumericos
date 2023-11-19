import math

#def f(x):
    #return ;

def rFalse(xl,xu):
    ea=100 #Error
    i=1
    xold=0
    xr=3
    while ea>10**-12 and i<=1000: #and f(xr)!=0:
        xr=xu-(f(xu)*(xl-xu))/(f(xl)-f(xu))
        ea=abs(((xr-xold)/xr))*100
        signo=f(xr)*f(xl)
        if signo<0:
            xu=xr
        else
            xl=xr
        
        xold=xr #PlaceHolder
        i+=1
    
    print('Numero de iteraciones por regla falsa: ',i)
    print('Error por regla false: ', ea)
    print('Raiz por regla falsa: ',xr)