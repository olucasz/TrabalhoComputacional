# vetor = [2,8,5,3,9,4,1]

def BubbleSort(vetor):
    # #Steps
    # #1. Compare consecutive items if out of place swap them
    # #2. The highest number will bubble to the right with it iteration
    swapped = False
    i=len(vetor)
    while(i!=0):
        for j in range(i-1):
            # Se o item da esquerda for menor que o item da direita
            if vetor[j] > vetor[j+1]:
                swapped = True
                #troca de lugar
                aux = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
                    
        #Acabou a iteracao
        # print(f"Bubble: {vetor}")
        i=i-1
        if not swapped:
            break

# BubbleSort(vetor)
# print(f"Final: {vetor}")