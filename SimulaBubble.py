# importa o arquivo bubbleSort
from BubbleSort import BubbleSort
# importa bibliotecas de graficos
import matplotlib.pyplot as plt
import numpy as np
import time

# Inicializa o vetor de tempo
tempos = []
for i in range(0,30):
    # Cria um vetor de 10000 a 0
    vetor = list(range(10000,0,-1))
    # # Embaralha o vetor
    # np.random.shuffle(vetor)
    # Inicia a contagem do tempo
    start_time = time.time()
    # Ordena o vetor
    BubbleSort(vetor)
    # Adiciona o tempo na lista de tempos
    tempos.append(time.time() - start_time)

print(tempos)

# Tempo médio necessário junto com o desvio padrão
print(f"Tempo médio: {np.mean(tempos)}")
print(f"Desvio padrão: {np.std(tempos)}")
