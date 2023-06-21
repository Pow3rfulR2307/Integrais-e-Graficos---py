import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

tempo = [0, 1, 2, 3, 4]
velocidade_lista= [0, 3, 4, 2, 0]
grafico_tempo = np.linspace(0, 5, 100)

polinomio = lagrange(tempo, velocidade_lista)

velocidade = polinomio(grafico_tempo)

aceleracao = np.gradient(velocidade, grafico_tempo)

posicao =  np.cumsum(velocidade) * np.mean(np.diff(grafico_tempo)) 

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(grafico_tempo, velocidade)
plt.scatter(tempo, velocidade_lista, color='red')
plt.axvline(x=5, color='black', linestyle='--')
plt.title('Gráfico de Velocidade')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')

plt.subplot(3, 1, 2)
plt.plot(grafico_tempo, aceleracao)
plt.axvline(x=5, color='black', linestyle='--')
plt.title('Gráfico de Aceleração')
plt.xlabel('Tempo (s)')
plt.ylabel('Aceleração (m/s^2)')

plt.subplot(3, 1, 3)
plt.plot(grafico_tempo, posicao)
plt.axvline(x=5, color='black', linestyle='--')
plt.title('Gráfico de Posição')
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')

plt.tight_layout()
plt.show()