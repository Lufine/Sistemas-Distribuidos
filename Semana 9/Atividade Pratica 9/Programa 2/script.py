import threading

# Definição do vetor de tamanho 1000
vec = list(range(1000))

# Escalar utilizado para multiplicar os elementos do vetor
scalar = 2

# Lista compartilhada para armazenar o vetor resultante
result = [0] * 1000

# Função que multiplica um bloco de 100 elementos do vetor pelo escalar
def multiply_block(start, end):
    for i in range(start, end):
        result[i] = vec[i] * scalar

# Lista para armazenar as threads
threads = []

# Criação das threads para multiplicar os elementos do vetor
for i in range(0, 1000, 100):
    thread = threading.Thread(target=multiply_block, args=(i, i+100))
    threads.append(thread)
    thread.start()

# Aguarda o término da execução de todas as threads
for thread in threads:
    thread.join()

# Exibição do vetor resultante na tela
print("Vetor resultante:")
print(result)
