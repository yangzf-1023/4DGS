import numpy as np
import matplotlib.pyplot as plt

def exp_opacity_decay(old_opacity, factor=0.99, offset=0.005, p=2):
    a = factor - offset
    b = 1 - offset
    if p != 0:
        return  (a + (b - a) * (1 - np.exp(p * old_opacity)) / (1 - np.exp(p)))
    else:
        return  (a + (b - a) * old_opacity)

# 设置参数
factor = 0.996
offset = 0.0
p_values = [-5, -2, -1, -0.5, -0.1, 0, 0.1, 0.5, 1, 2, 5]
opacity_range = np.linspace(0, 1, 100)

# 计算不同p值的输出
plt.figure(figsize=(10, 6))
for p in p_values:
    output_opacity = exp_opacity_decay(opacity_range, factor, offset, p)
    plt.plot(opacity_range, output_opacity, label=f'p={p}')

# 设置图表属性
plt.title('Exponential Opacity Decay (factor=0.99, offset=0.005)')
plt.xlabel('Input Opacity')
plt.ylabel('Output Opacity')
plt.legend()
plt.grid(True)
plt.ylim(factor, 1)
plt.savefig(f'exp_opacity_decay.png')