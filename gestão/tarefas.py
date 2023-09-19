import pandas as pd
import matplotlib.pyplot as plt


# Dias corridos
dias = [17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]

# Esforço planejado - ao menos 2 tarefas por dia
esforco_planejado = [34,32,30,28,26,24,22,20,18,16,14,12,10,8,6,4,2]

# Esforço realizado 
esforco_realizado = [34,31,31,25,24,23,21,20,20,19,19,15,15,11,8,5,0]

#  [::-1] técnica de indexação que inverte a ordem dos elementos na lista
plt.figure(figsize=(10, 6))
plt.plot(dias, esforco_planejado[::-1], label='Esforço Planejado', marker='o')
plt.plot(dias, esforco_realizado[::-1], label='Esforço Realizado', marker='x')
plt.title('Gráfico de Burndown')
plt.xlabel('Dias')
plt.ylabel('Esforço')
plt.legend()
plt.grid(True)
plt.show()


# Colaboração entre equipes

# Dados
colab_tarefas = [
    {'Equipe':'Dev Python','Tarefas Concluidas':8},
    {'Equipe': 'Databank','Tarefas Concluidas':7},
    {'Equipe':'Business Intelligence','Tarefas Concluidas':11}
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
