import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation



def f(x, y):
    return x**2 + y**2


def f_gradient(x, y):
    df_dx = 2 * x  
    df_dy = 2 * y  
    return np.array([df_dx, df_dy])

#  Gradient Descent  

def gradient_descent_3d(start_x, start_y, learning_rate, n_iterations):
   
    history = []
    x, y = start_x, start_y
    
    for _ in range(n_iterations):
        z = f(x, y)
        
        history.append((x, y, z))
        
        gradient = f_gradient(x, y)
        
        x = x - (learning_rate * gradient[0])
        y = y - (learning_rate * gradient[1])
        
    return history

#  Run 

learning_rate = 0.1
n_iterations = 30
start_x = -8.0  # Starting x
start_y = 8.0   # Starting y

history = gradient_descent_3d(start_x, start_y, learning_rate, n_iterations)

x_history = [step[0] for step in history]
y_history = [step[1] for step in history]
z_history = [step[2] for step in history]

#  Set up  3D 

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Set plot limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(0, 150)
ax.set_title("3D Gradient Descent Animation")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y) = x^2 + y^2")

# Plot Static Function Surface ---

# Create a meshgrid to plot the surface
X = np.linspace(-10, 10, 100)
Y = np.linspace(-10, 10, 100)
X_mesh, Y_mesh = np.meshgrid(X, Y)
Z_mesh = f(X_mesh, Y_mesh)


ax.plot_surface(X_mesh, Y_mesh, Z_mesh, cmap='viridis', alpha=0.6, 
                edgecolor='none', label="f(x, y)")

# Set up  Animated Element ---


point, = ax.plot([], [], [], 'ro', markersize=10, label="Current Position")
path, = ax.plot([], [], [], 'r--', linewidth=2, label="Path Taken")


dummy_surface = plt.Line2D([0],[0], linestyle="none", c='blue', marker='_')
ax.legend([dummy_surface, point, path], 
          ['f(x, y) = x^2 + y^2', 'Current Position', 'Path Taken'], numpoints=1)

#  Animation Function ---

def update(frame):

    point.set_data_3d([x_history[frame]], [y_history[frame]], [z_history[frame]])
    
   
    path.set_data_3d(x_history[:frame+1], y_history[:frame+1], z_history[:frame+1])
    
    return point, path

#  Create and Display the 

ani = FuncAnimation(fig, update, frames=len(x_history), 
                    interval=100, blit=False)


plt.show()

print(f"Algorithm start: (x, y) = ({start_x}, {start_y})")
print(f"Minimum found (x, y) = ({x_history[-1]:.4f}, {y_history[-1]:.4f})")