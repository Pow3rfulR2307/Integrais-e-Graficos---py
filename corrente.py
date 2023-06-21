import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

x = sy.symbols("x")
x_graph = np.linspace(0, 2, 100)

v1 = x**2

v2 = (x**2) - 2*x + 1

ddp1 = sy.integrate(v1, (x, 0, 2))
ddp2 = sy.integrate(v2, (x, 0, 2))

ddpNumerico1 = sy.N(ddp1) 
ddpNumerico2 = sy.N(ddp2)

valores_grafico1 = sy.lambdify(x, v1)
valores_grafico2 = sy.lambdify(x, v2)

grafico1 = valores_grafico1(x_graph)
grafico2 = valores_grafico2(x_graph)

plt.fill_between(x_graph, grafico1, grafico2, where=(grafico1 > grafico2), interpolate=True, alpha=0.4)

print("1:",ddpNumerico1,"2:",ddpNumerico2)

plt.plot(x_graph, grafico1)
plt.plot(x_graph, grafico2)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()