import time

def TorresDeHanoi(n, origen, destino, auxiliar, mostrar=False):
    if n == 1:
        if mostrar:
            print(f'mueve el disco 1 de {origen} a {destino}')
        return
    TorresDeHanoi(n-1, origen, auxiliar, destino, mostrar)
    if mostrar:
        print(f'mueve el disco {n} de {origen} a {destino}')
    TorresDeHanoi(n-1, auxiliar, destino, origen, mostrar)

def medir(n):
    inicio = time.perf_counter()
    TorresDeHanoi(n, 'A', 'B', 'C')
    fin = time.perf_counter()
    print(f'{n} discos: {fin - inicio:.6f} s | movimientos: {2**n - 1:,}')


medir(30)