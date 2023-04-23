import logging
import threading
import time
import random
import numpy as np


def somar_matrizes_thread(matriz1, matriz2, result, thread_idx, numthreads):
    tamlinha = matriz1.shape[0]
    row_step = tamlinha // numthreads                               #dividindo o tamanho da linha pelo número de threads para encontrar o trabalho das threads
    start_row = thread_idx * row_step                               #thread_idx é o índice da thread atual
    end_row = start_row + row_step if thread_idx != numthreads - 1 else tamlinha        #Confere se o passo atual já terminou de calcular tudo
    
    result[start_row:end_row, :] = matriz1[start_row:end_row, :] + matriz2[start_row:end_row, :]        



def somar_matrizes(tamlinha, tamcoluna, numthreads):

    result = np.zeros((tamlinha, tamcoluna))
    threads = []


    for i in range(numthreads):
        th = threading.Thread(target=somar_matrizes_thread, args=(matriz1,matriz2,result, i, numthreads)) #inicializa a thread, informa o nome da função e os parâmetros
        threads.append(th)
        th.start()
        

    for t in threads:
        t.join()
    
    return result




if __name__ == "__main__" :
    tamlinha = int(input("Digite quantas linhas as matrizes devem ter : "))
    tamcoluna = int(input("Digite quantas colunas as matrizes devem ter : "))
    numthreads = int(input("Digite o número de threads desejado: "))

    matriz1 = np.random.randint(10, size=(tamlinha, tamcoluna))
    matriz2 = np.random.randint(10, size=(tamlinha, tamcoluna))

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    
    
    
    result = somar_matrizes(tamlinha, tamcoluna, numthreads)
    
    print("")
    print(matriz1)
    print("")
    print("      +      ")
    print("")
    print(matriz2)
    print("")
    print("      =      ")
    print("")
    print(result)
