# vetor = [2,8,5,3,9,4]

def InsertionSort(vetor):
    #Steps
    #1. Work left to right
    #2. Examine each item and compare it to items on its left
    #3. Insert the item in the correct position in the array
    for i in range(0, len(vetor)):
        j=i
        # Enquanto não for o primeiro item do vetor
        # print(f"Analisando: {itemDireita}, Vetor: {vetor}")
        while(j!=0):
            # Se o item da direita for menor que o da esquerda
            if vetor[j] < vetor[j-1]:
                # Troca de lugar
                aux = vetor[j-1]
                vetor[j-1] = vetor[j]
                vetor[j] = aux
                # print(f"Troca de |{vetor[j-1]}| com |{vetor[j]}|: {vetor}")
            j=j-1

# InsertionSort(vetor)
# print(f"Final: {vetor}")


