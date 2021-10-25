def buscaBinaria(vetor, key, i = 0, F = None):
    if (F == None):
        F = len(vetor) -1

    if (F < i):
        return -1
    
    meio = (i + F) // 2
    if (vetor[meio] == key):
        return meio
    
    if (vetor[meio] > key):
        F = meio -1
    else:
        i = meio +1
    return buscaBinaria(vetor, key, i, F)


vetor = [ 2, 3, 4, 10, 40 ]
print('Digite a chave de busca: ')
key = int(input('>> '))

resultado = buscaBinaria(vetor, key, 0, len(vetor)-1)

if resultado != -1:
	print("Elemento presente na posição", str(resultado))
else:
	print("Elemento não está presente no vetor")

