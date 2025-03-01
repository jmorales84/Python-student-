import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Configuración de la figura y el eje
fig, ax = plt.subplots()
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Configuración de los vectores
line1, = ax.plot([], [], lw=2, label='Counterclockwise')
line2, = ax.plot([], [], lw=2, label='Clockwise')

# Inicialización de la función
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Función de actualización para la animación
def update(frame):
    x1 = np.cos(frame)
    y1 = np.sin(frame)
    line1.set_data([0, x1], [0, y1])

    x2 = np.cos(-frame)
    y2 = np.sin(-frame)
    line2.set_data([0, x2], [0, y2])

    return line1, line2

# Creación de la animación
frames = np.linspace(0, 2 * np.pi, 360)
ani = FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Mostrar la animación
plt.legend()
plt.show()
