import threading

# Função que conta e exibe os números de 1 a 500, de forma crescente
def count_up():
    for i in range(1, 501):
        print(i)

# Função que conta e exibe os números de 500 a 1, de forma decrescente
def count_down():
    for i in range(500, 0, -1):
        print(i)

# Criação das threads
thread1 = threading.Thread(target=count_up)
thread2 = threading.Thread(target=count_down)

# Início da execução das threads
thread1.start()
print('\n-----------------\n')
thread2.start()

# Aguarda o término da execução das threads
thread1.join()
thread2.join()