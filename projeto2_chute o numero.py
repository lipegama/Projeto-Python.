#projet 2 - Chute o número
'''
Escreva um programa que, ao iniciar, gere um valor aleatório de 1 a 10 e permita 
que o usuário chute números até acertar o valor gerado.

O programa deve informar se o chute foi maior, menor ou igual ao valor aleatório
gerado no inicio.
'''
# Método 5q para montar um agoritimo
'''
# Problema - Gastos totais com pagamento de salários.
# Dado uma lista de salários, calcule o total pago a todos os funcionários

# Método 5Q's para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- o número(chute) do usuário

2. O que devo fazer com estes dados?
comparar com o valor aleatório e verificar se o usuário chutou correto

3. Quais são as restrições deste problema?
Gerar o valor aleatório de 1 a 10
permitir que o usuario chute sem restrições de quantidade      

4. Qual é o resultado esperado?
exibir se o valor que usuário passou está abaixo ou acima ou igual o valor gerado
 

5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
(pseudocódigo)
-Gerar o valor aleatorio de 1 a 10
-permitir que o usuario chute numero quantas vezes quiser
-emitir mensagem se está perto ou longe no numero aleatório

''' 

import random

valor_aleatorio = random.randint(1,10)
acertou = False

while acertou == False:
    chute = int (input('Chute um numero:'))
    if chute > valor_aleatorio:
        print('Chute um valor um valor mais baixo')
    elif chute < valor_aleatorio:
        print('Chute um valor mais alto')
    else:
        print('Você acertou')
        acertou = True