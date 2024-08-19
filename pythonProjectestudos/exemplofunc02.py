def intersetado (seq1,seq2): # A função intersetado recebe dois argumentos
    res=[]                   # Criei uma lista vazia
    for x in seq1:           # Itera sobre cada elemento 'x' da primeira sequência seq1.
        if x in seq2:        # Verifica se o elemento 'x' está presente na segunda sequência 'seq2'
            res.append(x)    # Adiciona o elemento x à lista res se ele estiver presente em seq2.

    return res               # Retorna a lista 'res' após o primeiro elemento que satisfaz a condição de estar em ambas as sequências.


seq1 = [1, 2, 3, 4, 5]       # Elementos da sequência 'seq1'
seq2 = [3, 4, 5, 6, 7]       # Elementos da sequência 'seq2'

print(intersetado(seq1, seq2))  # Saída: [3, 4, 5]

