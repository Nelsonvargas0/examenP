#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 06:28:24 2024

@author: nelsonvargas
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros y constantes
alpha = -0.5
beta = 1
C1 = 5
C2 = 2.5

# Función para el desplazamiento x(t)
def desplazamiento(t):
    return np.exp(alpha * t) * (C1 * np.cos(t) + C2 * np.sin(t))

# Función para la velocidad v(t)
def velocidad(t):
    return np.exp(alpha * t) * (-C1 * np.sin(t) + C2 * np.cos(t)) + alpha * np.exp(alpha * t) * (C1 * np.cos(t) + C2 * np.sin(t))

# Tiempo de simulación
t = np.linspace(0, 10, 400)

# Calcular el desplazamiento y la velocidad
x_t = desplazamiento(t)
v_t = velocidad(t)

# a) Calcular el tiempo para que el factor de amortiguación disminuya al 50%
factor_amortiguacion = 0.5
tiempo_50 = np.log(factor_amortiguacion) / alpha

# b) Calcular el porcentaje de disminución del factor de amortiguación después de un periodo
T = 2 * np.pi
factor_amortiguacion_periodo = np.exp(alpha * T)
porcentaje_disminucion = (1 - factor_amortiguacion_periodo) * 100

# c) Calcular la posición y la velocidad después de un periodo
x_T = desplazamiento(T)
v_T = velocidad(T)

# Mostrar resultados
print(f"a) El tiempo requerido para que el factor de amortiguación disminuya al 50% es: {tiempo_50:.4f} segundos")
print(f"b) El porcentaje de disminución del factor de amortiguación después de un periodo es: {porcentaje_disminucion:.2f}%")
print(f"c) La posición de la partícula después de un periodo es: {x_T:.4f} metros")
print(f"c) La velocidad de la partícula después de un periodo es: {v_T:.4f} m/s")

# Graficar el desplazamiento contra el tiempo
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x_t, label='x(t)')
plt.xlabel('Tiempo t (s)')
plt.ylabel('Desplazamiento x(t) (m)')
plt.title('Desplazamiento de la partícula en función del tiempo')
plt.legend()
plt.grid(True)

# Graficar la velocidad contra el tiempo
plt.subplot(2, 1, 2)
plt.plot(t, v_t, label='v(t)', color='r')
plt.xlabel('Tiempo t (s)')
plt.ylabel('Velocidad v(t) (m/s)')
plt.title('Velocidad de la partícula en función del tiempo')
plt.legend()
plt.grid(True)

# Mostrar las gráficas
plt.tight_layout()
plt.show()
