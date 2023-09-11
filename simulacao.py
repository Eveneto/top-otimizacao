import random
import matplotlib.pyplot as plt

# Número de passageiros
n_passageiros = 5000

# Faixas de carga
faixas_de_carga = ["0-3 kg", "4-7 kg", "8-11 kg", "12-15 kg", "16-19 kg", "Acima de 19 kg"]

# Probabilidades de cada faixa de carga
# Por exemplo, 20% de chance de 0-3 kg, 30% de chance de 4-7 kg, 25% de chance de 8-11 kg, 15% de chance de 12-15 kg, 8% de chance de 16-19 kg, 2% de chance de acima de 19 kg
probabilidades = [0.20, 0.30, 0.25, 0.15, 0.08, 0.02]

# Inicialize contadores para cada faixa de carga
contadores = [0] * len(faixas_de_carga)

# Gere dados fictícios para cada passageiro com base nas probabilidades
for _ in range(n_passageiros):
    carga = random.choices(faixas_de_carga, weights=probabilidades)[0]
    if carga == "0-3 kg":
        contadores[0] += 1
    elif carga == "4-7 kg":
        contadores[1] += 1
    elif carga == "8-11 kg":
        contadores[2] += 1
    elif carga == "12-15 kg":
        contadores[3] += 1
    elif carga == "16-19 kg":
        contadores[4] += 1
    else:
        contadores[5] += 1

# Calcule as porcentagens
porcentagens = [contagem / n_passageiros * 100 for contagem in contadores]

# Define o limite máximo do eixo y para 100%
plt.ylim(0, 100)

# Crie um gráfico de barras
plt.bar(faixas_de_carga, porcentagens)
plt.xlabel('Faixa de Carga (kg)')
plt.ylabel('Porcentagem de Passageiros (%)')
plt.title('Distribuição de Carga por Passageiros em um Avião')

# Mostrar o gráfico
plt.show()
