# vetor = [2,8,5,3,9,4,1]

def SelectionSort(vetor):
    #During each iteration we'll select the smallest item from the unsorted partition and move it to the sorted partition
    #Steps
    #1. Set the current item as the minimum
    #2. Progress into the array looking for a smallest number
    #3. If find a lower number, set as the current item and current minimum and swap them
    # print(f"Comeco: {vetor}")
    for i in range(0, len(vetor)):
        currentItem = i
        currentMinimum = vetor[i]
        for j in range(i, len(vetor)):
            # Se o item atual for menor que o minimo, então
            if vetor[j] < currentMinimum:
                # Define o novo minimo
                currentMinimum = vetor[j]
                # Salva a posicao
                currentItem = j
                
        # Se o minimo for diferente do item atual, então
        if vetor[i] != currentMinimum:
            # Troca de lugar
            aux = vetor[i]
            vetor[i] = vetor[currentItem]
            vetor[currentItem] = aux
            # print(f"Troca: {vetor}")

# SelectionSort(vetor)
# print(vetor)
            
