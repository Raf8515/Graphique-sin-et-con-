import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

x_values = np.linspace(0, 30, 1500)
y_values_sin = np.sin(x_values)
y_values_cos = np.cos(x_values)

print("Tableau des valeurs de x, sin(x) et cos(x) :")

x_mod = []
y_mod_sin = []
y_mod_cos = []

i = 0
j = 100
while i < len(x_values):
    if i % j == 0:
        print(f"x[{i}] = {x_values[i]:.2f}, sin(x) = {y_values_sin[i]:.2f}, cos(x) = {y_values_cos[i]:.2f}")
        x_mod.append(x_values[i])
        y_mod_sin.append(y_values_sin[i])
        y_mod_cos.append(y_values_cos[i])
    i += 1

fig = plt.figure(figsize=(12, 12))

ax1 = fig.add_axes([0.1, 0.55, 0.8, 0.35])
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.35])

ax1.plot(x_values, y_values_sin, label='sin(x)', color='b', linewidth=2)
ax1.scatter(x_mod, y_mod_sin, color='black', marker='x')
ax1.axhline(0, color='black', linewidth=1, linestyle='--')
ax1.set_title('Fonction sinus')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.set_xlim([0, 30])
ax1.set_ylim([-1.1, 1.1])
ax1.legend()
ax1.grid(True)

ax2.plot(x_values, y_values_cos, label='cos(x)', color='r', linewidth=2)
ax2.scatter(x_mod, y_mod_cos, color='black', marker='x')
ax2.axhline(0, color='black', linewidth=1, linestyle='--')
ax2.set_title('Fonction cosinus')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.set_xlim([0, 30])
ax2.set_ylim([-1.1, 1.1])
ax2.legend()
ax2.grid(True)

grid_visible = True
ticks_visible = True

def toggle_grid(event):
    global grid_visible
    grid_visible = not grid_visible
    ax1.grid(grid_visible)
    ax2.grid(grid_visible)
    plt.draw()

def toggle_ticks(event):
    global ticks_visible
    ticks_visible = not ticks_visible
    ax1.xaxis.set_visible(ticks_visible)
    ax1.yaxis.set_visible(ticks_visible)
    ax2.xaxis.set_visible(ticks_visible)
    ax2.yaxis.set_visible(ticks_visible)
    plt.draw()

ax_toggle_grid = plt.axes([0.8, 0.95, 0.1, 0.04])
visible_checkbox_grid = Button(ax_toggle_grid, 'Grille ON/OFF', color='lightgray', hovercolor='lightblue')
visible_checkbox_grid.on_clicked(toggle_grid)

ax_toggle_ticks = plt.axes([0.6, 0.95, 0.15, 0.04])
visible_checkbox_ticks = Button(ax_toggle_ticks, 'Axes ON/OFF', color='lightgray', hovercolor='lightblue')
visible_checkbox_ticks.on_clicked(toggle_ticks)

plt.show()
