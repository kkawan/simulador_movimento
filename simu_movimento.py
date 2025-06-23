import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Aplicar o estilo do Seaborn
sns.set(style="darkgrid")

# Definição simbólica
t = sp.symbols('t')
s = t**3 - 6*t**2 + 9*t
v = sp.diff(s, t)
a = sp.diff(v, t)
#Outro exemplo pode ser a função s(t) = t**4 - 4*t**3 + 4*t**2 (função polinomial de quarto grau)

# Mostrar funções
print(f"s(t) = {s}")
print(f"v(t) = {v}")
print(f"a(t) = {a}")

# Funções numéricas
s_func = sp.lambdify(t, s, 'numpy')
v_func = sp.lambdify(t, v, 'numpy')
a_func = sp.lambdify(t, a, 'numpy')

# Intervalo de tempo
t_vals = np.linspace(0, 10, 400)
s_vals = s_func(t_vals)
v_vals = v_func(t_vals)
a_vals = a_func(t_vals)

# DataFrame para Seaborn
df = pd.DataFrame({
    'Tempo': t_vals,
    'Posição': s_vals,
    'Velocidade': v_vals,
    'Aceleração': a_vals
})

# Criar subplots
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Posição
sns.lineplot(ax=axes[0], x='Tempo', y='Posição', data=df, color='blue')
axes[0].set_title('Posição s(t)')
axes[0].axhline(0, color='black', linestyle='--', linewidth=0.7)
axes[0].set_ylabel('s(t)')

# Velocidade
sns.lineplot(ax=axes[1], x='Tempo', y='Velocidade', data=df, color='green')
axes[1].set_title('Velocidade v(t)')
axes[1].axhline(0, color='black', linestyle='--', linewidth=0.7)
axes[1].set_ylabel('v(t)')

# Aceleração
sns.lineplot(ax=axes[2], x='Tempo', y='Aceleração', data=df, color='red')
axes[2].set_title('Aceleração a(t)')
axes[2].axhline(0, color='black', linestyle='--', linewidth=0.7)
axes[2].set_ylabel('a(t)')
axes[2].set_xlabel('Tempo (t)')

# Ajuste final
plt.tight_layout()
plt.show()
