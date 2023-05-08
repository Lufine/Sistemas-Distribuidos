import threading

# Definição da matriz 5x5
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

# Função que calcula a soma dos elementos de uma linha da matriz e armazena em uma lista compartilhada
def sum_line(line, results):
    result = sum(line)
    results.append(result)

# Lista compartilhada para armazenar os resultados das somas das linhas
results = []

# Lista para armazenar as threads
threads = []

# Criação das threads para calcular a soma de cada linha da matriz
for i in range(5):
    thread = threading.Thread(target=sum_line, args=(matrix[i], results))
    threads.append(thread)
    thread.start()

# Aguarda o término da execução de todas as threads
for thread in threads:
    thread.join()

# Exibição dos resultados na tela
print("Somas das linhas da matriz:")
for i in range(5):
    print(f"Linha {i+1}: {results[i]}")
