import numpy as np
import matplotlib.pyplot as plt
import plotext as plt_ext

# Задаем диапазон x
x = np.linspace(-10, 10, 100)

# Кубическое уравнение y = ax^3 + bx^2 + cx + d
a = 1
b = -2
c = 3
d = -4
y = a * x**3 + b * x**2 + c * x + d

# Построение графика с помощью matplotlib
plt.plot(x, y, label=f'{a}x^3 + {b}x^2 + {c}x + {d}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График кубического уравнения')
plt.legend()
plt.grid(True)
plt.show()

# Построение графика с помощью plotext
plt_ext.plot(x, y)
plt_ext.title('График кубического уравнения')
plt_ext.show()
