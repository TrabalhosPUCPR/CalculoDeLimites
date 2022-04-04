import sympy as sp

esc = input('Digite a letra do exercicio ')
print(esc)

if esc == "a":
    x = sp.Symbol('x')

    funcao = x**2-4
    lim = sp.limit(funcao, x, 2)


if esc == "b":
    x = sp.Symbol('x')

    funcao = (x**3-4*x)/(2*x**2 + 3*x)
    lim = sp.limit(funcao, x, 0)


if esc == "c":
    x = sp.Symbol('x')

    funcao = x**3/((x+1)**2)
    lim = sp.limit(funcao, x, 1)


    
print(lim)
sp.plot(funcao, line_color="red")