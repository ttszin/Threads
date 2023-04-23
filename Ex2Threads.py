import logging
import threading
import time
import random
import numpy as np


if __name__ == "__main__" :
    tamlinha = int(input("Digite quantas linhas as matrizes devem ter : "))
    tamcoluna = int(input("Digite quantas colunas as matrizes devem ter : "))

    matriz1 = np.zeros((tamlinha,tamcoluna), dtype=np.float64)
    matriz2 = np.zeros((tamlinha,tamcoluna), dtype=np.float64)

    print(matriz1,"\n\n", matriz2)