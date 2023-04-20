import logging
import threading
import time
import random


def thread_function(id,vetor1, vetor2, inicio, fim):    
    i = 0
    for i in range(fim):
        saida[i] = vetor1[i]+vetor2[i]
        print("Saída = ",saida)
        print("Vetor2 = ",vetor2)

    
   



if __name__ == "__main__":  

    num1 = int(input('Digite o tamanho dos vetores : '))
    num_threads = int(input("Digite o número de threads: "))


    vetor1 = [random.randint(0, 100) for _ in range(num1)]
    vetor2 = [random.randint(0, 100) for _ in range(num1)]
    saida = [0 for _ in range(num1)]

    threadsnecessarias = num1//num_threads                            #Dividindo o tamanho do vetor pela quantidade de threads
    inicio = 0
    fim = threadsnecessarias



    threads = [] #armazena os descritores das threads

    for i in range(num_threads):
        t = threading.Thread(target=thread_function, args=(vetor1, vetor2, saida, inicio, fim))
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
    print(saida)