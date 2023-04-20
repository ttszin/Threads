import logging
import threading
import time
import random


def thread_function(id,vetor1, vetor2, inicio, fim, saida):
    
    for i in range(inicio,fim):
        saida[i] = vetor1[i] + vetor2[i]

        print(f"{vetor1[i]} + {vetor2[i]} = {saida[i]}")


if __name__ == "__main__":  

    num1 = int(input('Digite o tamanho dos vetores : '))
    num_threads = int(input("Digite o número de threads: "))


    vetor1 = [random.randint(0, 100) for _ in range(num1)]
    vetor2 = [random.randint(0, 100) for _ in range(num1)]
    print(f'v1: {vetor1}\nv2: {vetor2}')
    saida = [0 for _ in range(num1)]
    print(f'saida: {saida}')
    threadsnecessarias = num1//num_threads                            #Dividindo o tamanho do vetor pela quantidade de threads
    inicio = 0
    fim = threadsnecessarias



    threads = [] #armazena os descritores das threads

    for i in range(num_threads):
        t = threading.Thread(target=thread_function, args=(i,vetor1, vetor2, inicio, fim, saida))
        threads.append(t)
        inicio = fim
        fim += threadsnecessarias

    # Inicia as threads
    for t in threads:
        t.start()

    # Comando para esperar até que todas as threads tenham terminado
    for t in threads:
        t.join()


    print(vetor1,'+',vetor2,"=",saida)
    #print(saida)