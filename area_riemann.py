import sympy as sy
import matplotlib.pyplot as plt
import numpy as np

a = 2.5
b =7

x = sy.symbols("x")
x_graph = np.linspace(a, b, 100)

f_a = 40*(x**3) + 12*(x**2) - 9*x

f_np = sy.lambdify(x, f_a)
valor_grafico = f_np(x_graph)

integral_a = sy.integrate(f_a, (x, a, b))
print(f"Área a: {integral_a.evalf()}")

n = 10000
x_riemann = np.linspace(a, b, n+1)
y_riemann = f_np(x_riemann)
delta_x = (b - a) / n
area_riemann = np.sum(y_riemann) * delta_x
print("Área calculada usando soma de Riemann:", area_riemann)

plt.plot(x_graph, valor_grafico, label='f(x)')
plt.fill_between(x_graph, valor_grafico, 0, where=(x_graph >= a) & (x_graph <= b), alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico da Letra a')
plt.legend()
plt.grid(True)
plt.show()