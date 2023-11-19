from sympy import diff, symbols, factorial, tan, exp, pretty_print, sec, cos, sin, pi
from sympy.plotting import plot

x = symbols('x')  # symbol

func = cos(x) - x  # function
funcDiff = diff(func, x)
p0 = 0.2  # initial point
n = 5  # This is an Example
error = 100
i = 1

while error > 10 ** -12 and i <= 1000 and func.subs(x, p0) != 0:
    p = p0 - func.subs(x, p0) / funcDiff.subs(x, p0)
    error = abs((p - p0) / p)*100
    p0 = p
    print('Value of the function at ', i, ' times:', p)
    print('Error:', float(error))
    i += 1

p1 = plot(func, (x, -5, 5), show=False, title='Graph of the function', ylim=[-5, 5])
p1.show()
