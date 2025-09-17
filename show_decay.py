import numpy as np
import matplotlib.pyplot as plt
import math

# 定义参数
f_min = 0.995
f_max = 1.0
p_values = [0, 0.5, 1, 2]  # 不同 p 值用于测试
old_opacity = np.linspace(0, 1, 1000)  # old_opacity 从 0 到 1

# 初始化存储系数的字典
coefficients = {
    'const': [],
    'exp_asc': {p: [] for p in p_values},
    'exp_desc': {p: [] for p in p_values},
    'power_asc': {p: [] for p in p_values},
    'power_desc': {p: [] for p in p_values}
}

# 计算每个模式下的系数
for opacity in old_opacity:
    # const 模式
    coeff_const = f_min
    coefficients['const'].append(coeff_const)

    # # exp_asc 模式
    # for p in p_values:
    #     if p != 0:
    #         coeff_exp_asc = f_min + (f_max - f_min) * (1 - np.exp(p * opacity)) / (1 - math.exp(p))
    #     else:
    #         coeff_exp_asc = f_min + (f_max - f_min) * opacity 
    #     coefficients['exp_asc'][p].append(coeff_exp_asc)

    # # exp_desc 模式
    # for p in p_values:
    #     if p != 0:
    #         coeff_exp_desc = f_min + (f_max - f_min) * ((np.exp(-p * opacity) - math.exp(-p)) / (1 - math.exp(-p)))
    #     else:
    #         coeff_exp_desc = f_min + (f_max - f_min) * (1 - opacity)
    #     coefficients['exp_desc'][p].append(coeff_exp_desc)

    # power_asc 模式
    for p in p_values:
        if p <= 0:
            continue
        coeff_power_asc = f_min + (f_max - f_min) * (opacity ** p)
        coefficients['power_asc'][p].append(coeff_power_asc)

    # power_desc 模式
    for p in p_values:
        if p <= 0:
            continue
        coeff_power_desc = f_min + (f_max - f_min) * ((1 - opacity) ** p)
        coefficients['power_desc'][p].append(coeff_power_desc)

# 绘制图形
plt.figure(figsize=(12, 8))

# 绘制 const 模式
plt.plot(old_opacity, coefficients['const'], label='const', linestyle='--')

# # 绘制 exp_asc 模式
# for p in p_values:
#     plt.plot(old_opacity, coefficients['exp_asc'][p], label=f'exp_asc (p={p})')

# # 绘制 exp_desc 模式
# for p in p_values:
#     plt.plot(old_opacity, coefficients['exp_desc'][p], label=f'exp_desc (p={p})')

# 绘制 power_asc 模式
for p in p_values:
    plt.plot(old_opacity, coefficients['power_asc'][p], label=f'power_asc (p={p})')

# 绘制 power_desc 模式
for p in p_values:
    plt.plot(old_opacity, coefficients['power_desc'][p], label=f'power_desc (p={p})')

# 设置图形属性
plt.xlabel('Old Opacity')
plt.ylabel('Coefficient')
plt.title('Opacity Decay Coefficients vs Old Opacity')
plt.legend()
plt.grid(True)
plt.tight_layout()

# 保存并显示图形
plt.savefig('opacity_decay_coefficients.png')
plt.show()