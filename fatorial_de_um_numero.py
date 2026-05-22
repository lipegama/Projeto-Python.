#projeto 1 - Fatorial de um numero
#Crie um programa que recebe um numero e imprime o seu fatorial

# Método 5Q's para montar um algoritmo:


#1. Quais são os dados de entrada necessários?

#2. O que devo fazer com estes dados?

#3. Quais são as restrições deste problema?

#4. Qual é o resultado esperado?

#5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
'''
(pseudocódigo)
Receber o valor do usuario
verificar se é um numero positivo ou inteiro
pagar o valor do fatorial e muliplicar ate chegar no numero exato
exibir o valor na tela

'''


numero = int (input('Digite o fatorial que deseja calcular: '))
if numero > 0 and type(numero) == int:
    fatorial = 1
    for item in range(1, numero+1):
       print(f'{fatorial} * {item}') 
       fatorial = fatorial * item
       print(f'{fatorial}')
    print(f'o fatorial de {numero} é {fatorial}')
else:
    print('favor informar apenas números inteiros positivos')

    