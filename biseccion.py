from sympy import diff, symbols, factorial, tan, exp, pretty_print, sec, cos, sin, pi
from sympy.plotting import plot

x = symbols('x')  # symbol

func = cos(x) - x  # function

x0 = 0  # Initial
xf = 1  # Final
error = 100
i = 1
p = 1  # Example

while error > 10 ** -12 and i <= 1000 and func.subs(x, p) != 0:
    p = x0 + (xf - x0)/2
    if func.subs(x, p) * func.subs(x, x0) > 0:
        error = abs((p - x0) / p) * 100
        x0 = p
    else:
        error = abs((p - xf) / p) * 100
        xf = p

    print('Value of the root at ', i, ' times:', p)
    print('Error:', float(error))
    i += 1

# p1 = plot(func, (x, -5, 5), show=False, title='Graph of the function', ylim=[-5, 5])
# p1.show()
