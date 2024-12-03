import numpy as np
import matplotlib.pyplot as plt

# Dados
N = 9  # Número de elementos (pode ser ajustado conforme necessário)
h = 0.1  # Passo no eixo x
Tbegin = 60  # Temperatura inicial
Tend = 40  # Temperatura final

# Definindo a distância (eixo x)
x_barra = [i*h for i in range(N + 2)]

# Gerar a matriz de temperaturas (N + 2 linhas e N + 2 colunas)
# Aqui, a primeira linha é Tbegin, a última é Tend, e as intermediárias são aleatórias
T = np.random.rand(N + 2, N + 2) * 50  # Criando uma matriz aleatória de 0 a 50 para simular as temperaturas

# Colocando as temperaturas inicial e final nas bordas
T[0, :] = Tbegin  # Temperatura inicial
T[-1, :] = Tend   # Temperatura final

# Parâmetros do gráfico
altura = 0.5
norm = plt.Normalize(T.min(), T.max()) 
colors = plt.cm.Reds(norm(T))

# Criando o gráfico
plt.figure(figsize=(12, 6))  # Aumentando a altura para mais camadas de tempo

# O tempo será o eixo y e a distância será o eixo x
for t in range(N + 2):  # Para cada instante de tempo (linha da matriz T)
    # Empilhando as barras para cada "tempo"
    for i in range(N + 2):  # Para cada ponto no eixo x
        plt.fill_between(x_barra[i:i+3], t * altura, (t + 1) * altura, color=colors[t, i], alpha=0.7)

    # Adicionando o texto da temperatura acima das barras
    for i in range(N + 2):
        plt.text(x_barra[i], (t + 0.5) * altura, f'{T[t, i]:.1f}°', 
                 horizontalalignment='left', verticalalignment='center', 
                 fontsize=8, color='black')

# Ajustando os limites dos eixos
plt.xlim(0, 1)
#plt.ylim(0, N + 1)  # Ajustando a altura do gráfico para acomodar o tempo
plt.yticks([])  # Marcas do eixo y (tempo)
plt.xticks(x_barra)  # Marcas do eixo x (distância)
plt.xlabel('Distância')
plt.ylabel('Tempo')
plt.title('Distribuição de Temperaturas ao Longo do Tempo')

# Exibindo o gráfico
plt.show()
