import numpy as np
import threading
import random
import time

# Função que realiza a multiplicação de duas matrizes A e B
def multiply_matrices(A, B, result, i_start, i_end):
    for i in range(i_start, i_end):
        for j in range(B.shape[1]):
            result[i][j] = sum([A[i][k] * B[k][j] for k in range(B.shape[0])])

# Função principal do programa
def main():
    # Leitura das dimensões das matrizes e do número de threads
    M = int(input("Digite o número de linhas da matriz A: "))
    N = int(input("Digite o número de colunas da matriz A e o número de linhas da matriz B: "))
    P = int(input("Digite o número de colunas da matriz B: "))
    num_threads = int(input("Digite o número de threads: "))

    # Geração das matrizes A e B com valores aleatórios
    A = np.random.randint(10, size = (M, N))
    B = np.random.randint(10, size = (N, P))

    # Criação da matriz resultante com valores zerados
    result = np.zeros((M, P))

    # Cálculo do número de linhas a serem processadas por cada thread
    chunk_size = M // num_threads

    # Criação e inicialização das threads
    threads = []
    for i in range(num_threads):
        i_start = i * chunk_size
        i_end = i_start + chunk_size if i < num_threads - 1 else M
        t = threading.Thread(target=multiply_matrices, args=(A, B, result, i_start, i_end))
        threads.append(t)
        t.start()

    # Aguarda a finalização de todas as threads
    for t in threads:
        t.join()

    # Impressão das matrizes e do resultado
    print("Matriz A:")
    print(A)
    print("Matriz B:")
    print(B)
    print("Resultado da multiplicação:")
    print(result)

# Execução da função principal
if __name__ == '__main__':
    main()
