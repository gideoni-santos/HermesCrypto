import pandas as pd
import matplotlib.pyplot as plt


# Dias corridos
dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11 ,12 ,13 ,14 ,15 ,16 ,17]

# Esforço planejado - ao menos 2 tarefas por dia
esforco_planejado = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]

# Esforço realizado - media de 2 tarefas concluídas por dia
esforco_realizado = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]

# Calcular o esforço restante
esforco_restante = [esforco_planejado[i] - esforco_realizado[i] for i in range(len(dias))]

# Criar o gráfico de burndown
plt.figure(figsize=(10, 6))
plt.plot(dias, esforco_planejado, label='Esforço Planejado', marker='o')
plt.plot(dias, esforco_realizado, label='Esforço Realizado', marker='x')
plt.plot(dias, esforco_restante, label='Esforço Restante', marker='s')
plt.title('Gráfico de Burndown')
plt.xlabel('Dias')
plt.ylabel('Esforço')
plt.legend()
plt.grid(True)
plt.show()


# Colaboração entre equipes

# Dados
colab_tarefas = [
    {'Equipe':'Dev Python','Tarefas Concluidas':5},
    {'Equipe': 'Databank','Tarefas Concluidas':4},
    {'Equipe':'Business Intelligence','Tarefas Concluidas':7}
]

# Extrair nomes de equipe e tarefas concluídas
equipes = [item['Equipe'] for item in colab_tarefas]
tarefas_concluidas = [item['Tarefas Concluidas'] for item in colab_tarefas]

# Definir uma paleta de cores personalizada para as equipes
cores = ['blue', 'lightgreen', 'yellow']

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.bar(equipes, tarefas_concluidas, color=cores)  # Cria o gráfico de barras
plt.xlabel('Equipe')  # Rótulo do eixo x
plt.ylabel('Tarefas Concluídas')  # Rótulo do eixo y
plt.title('Colaboração entre equipes na conclusão de tarefas')  # Título do gráfico
plt.xticks(rotation=45)  # Rotaciona os rótulos no eixo x para melhor visualização
plt.grid(True)
plt.tight_layout()
plt.show()
