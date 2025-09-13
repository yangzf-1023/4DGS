import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x, factor, k=1):
    return 1 - (1 - factor) * np.sin(k * np.pi * x)**2

# 设置参数
factor = 0.996  # 最小值，可调整
x = np.linspace(0, 1, 1000)  # 定义域 [0,1]
k = 1
y = f(x, factor, k)

# 绘制图像
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'f(x) = 1 - (1 - {factor}) * sin²(πx)', color='blue')
plt.title('Function Plot')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.savefig('function_plot.png')