import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, cos, sin, pi
from sympy import plot_parametric

t = symbols('t')
a = 1  # Radio del círculo y factor de escala

# Funciones para el círculo y su involuta
def x_circle(t): return a * cos(t)
def y_circle(t): return a * sin(t)
def xi_circle(t): return a * (cos(t) + t*sin(t))
def yi_circle(t): return a * (sin(t) - t*cos(t))

# Funciones para la cicloide y su involuta
def x_cycloid(t): return t - sin(t)
def y_cycloid(t): return 1 - cos(t)
def xi_cycloid(t): return t + sin(t)
def yi_cycloid(t): return 3 + cos(t)

# Funciones para el asteroide y su involuta
def x_astroid(t): return cos(t)**3
def y_astroid(t): return sin(t)**3
def xi_astroid(t): return 1/8 * (3*cos(t) - cos(3*t))
def yi_astroid(t): return 1/8 * (3*sin(t) + sin(3*t))

# Funciones para la nefroide, su involuta y la séxtica de Cayley
def x_nephroid(t): return 1/2 * (3*cos(t) - cos(3*t))
def y_nephroid(t): return 1/2 * (3*sin(t) - sin(3*t))
def x_involute_nephroid(t): return 4 * cos(t)**3
def y_involute_nephroid(t): return 3*sin(t) + sin(3*t)
def x_cayley(t): return 4 * cos(t)**3 * (1 - 3/2 * sin(t)**2)
def y_cayley(t): return 4 * sin(t)**3 * (1 - 3/2 * cos(t)**2)

# Funciones para la parábola semicúbica y su involuta
def x_parabola(t): return t**2
def y_parabola(t): return a * t**3
def x_involute_parabola(t): return (t**2)/3 - 8/(27*a**2)
def y_involute_parabola(t): return -(4*t)/(9*a)

# Crear una figura con 5 subplots
fig, axs = plt.subplots(3, 2, figsize=(20, 30))

# Círculo y su involuta
p1 = plot_parametric(x_circle(t), y_circle(t), (t, 0, 2*pi), line_color='blue', show=False, label='Círculo')
p1._backend.ax = axs[0, 0]
p1._backend.process_series()
p2 = plot_parametric(xi_circle(t), yi_circle(t), (t, 0, 4*pi), line_color='red', show=False, label='Involuta del Círculo')
p2._backend.ax = axs[0, 0]
p2._backend.process_series()
axs[0, 0].set_title('Círculo y su Involuta')
axs[0, 0].legend()

# Cicloide y su involuta
p3 = plot_parametric(x_cycloid(t), y_cycloid(t), (t, -6*pi, 6*pi), line_color='blue', show=False, label='Cicloide')
p3._backend.ax = axs[0, 1]
p3._backend.process_series()
p4 = plot_parametric(xi_cycloid(t), yi_cycloid(t), (t, -6*pi, 6*pi), line_color='red', show=False, label='Involuta de la Cicloide')
p4._backend.ax = axs[0, 1]
p4._backend.process_series()
axs[0, 1].set_title('Cicloide y su Involuta')
axs[0, 1].legend()

# Asteroide y su involuta
p5 = plot_parametric(x_astroid(t), y_astroid(t), (t, 0, 2*pi), line_color='blue', show=False, label='Asteroide')
p5._backend.ax = axs[1, 0]
p5._backend.process_series()
p6 = plot_parametric(xi_astroid(t), yi_astroid(t), (t, 0, 2*pi), line_color='red', show=False, label='Involuta del Asteroide')
p6._backend.ax = axs[1, 0]
p6._backend.process_series()
axs[1, 0].set_title('Asteroide y su Involuta')
axs[1, 0].legend()

# Nefroide, su involuta y la séxtica de Cayley
p7 = plot_parametric(x_nephroid(t), y_nephroid(t), (t, 0, 2*pi), line_color='blue', show=False, label='Nefroide')
p7._backend.ax = axs[1, 1]
p7._backend.process_series()
p8 = plot_parametric(x_involute_nephroid(t), y_involute_nephroid(t), (t, 0, 2*pi), line_color='red', show=False, label='Involuta de la Nefroide')
p8._backend.ax = axs[1, 1]
p8._backend.process_series()
p9 = plot_parametric(x_cayley(t), y_cayley(t), (t, 0, 2*pi), line_color='green', show=False, label='Séxtica de Cayley')
p9._backend.ax = axs[1, 1]
p9._backend.process_series()
axs[1, 1].set_title('Nefroide, su Involuta y Séxtica de Cayley')
axs[1, 1].legend()

# Parábola semicúbica y su involuta
p10 = plot_parametric(x_parabola(t), y_parabola(t), (t, -2, 2), line_color='blue', show=False, label='Parábola Semicúbica')
p10._backend.ax = axs[2, 0]
p10._backend.process_series()
p11 = plot_parametric(x_involute_parabola(t), y_involute_parabola(t), (t, -2, 2), line_color='red', show=False, label='Involuta de la Parábola')
p11._backend.ax = axs[2, 0]
p11._backend.process_series()
axs[2, 0].set_title('Parábola Semicúbica y su Involuta')
axs[2, 0].legend()

# Eliminar el subplot vacío
fig.delaxes(axs[2, 1])

# Ajustar el diseño
plt.tight_layout()
plt.show()