import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the parabolic trajectory function
def parabolic_trajectory(t):
    x = t
    y = -0.5 * t**2 + 2 * t
    return x, y

# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(-2, 3)
line, = ax.plot([], [], 'ro')

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Update function for the animation
def update(frame):
    x, y = parabolic_trajectory(frame)
    line.set_data(x, y)
    return line,

# Generate the frames for the animation
frames = np.linspace(0, 4, 100)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=frames, init_func=init, blit=True, interval=50)

# Display the animation
plt.grid()
plt.title("Vector Parabolico")
plt.show()