def soma_todos_pares():     # Definindo a função 'soma_todos_pares' sem argumento
    soma=0                  # Inicializa a variável soma com o valor 0.
    for i in range(50,100): # Itera sobre cada número 'i' no intervalo de 50 a 99, inclusive.
        if i%2 == 0:        # Verificar se o número é par
            soma+= i        # Soma de todos os números pares
    return soma             # Retorna o valor da soma
print (soma_todos_pares())  # Imprimindo chamando a função 'soma_todos_pares'
