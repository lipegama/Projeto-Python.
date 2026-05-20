'''
#Variaveis
velocidade_internet = 400
print(velocidade_internet)
#Numeros inteiros(int)
idade = 15
#numeros decimais(float)
nota 8.5
#textos(string)(str)
nome_completo = 'Felipe Gama'
#booleanos
pode_entrar = True or False

print(type(idade))
'''
'''
1 quais são os dados de entrada necessários
-Salário Mensal
-Quantidade de horas trabalhadas

2 O que devo fazer com estes dados?
-Calcular o valor horas

3.Quais são as restrições deste problema?
-Precisa ter um valor Salário Mensal
-Precisa ter um valor da quantidade de horas trabalhadas

4. Qual é o resultado esperado?
-Exibir o valor hora da pessoa, com base no calculo de valor hora

5. Qual é a sequencia de passos a  ser feita para chegar ao resultado esperado?
(pseudocodigo)

Receber o salario Mensal
receber quantidade de horas trabalhadas
valor hora = salario mensal / quantidade de horas trabalhadas
exibir valor hora
'''


salario_mensal = input('Qual é o seu salário mensal: ')
horas_trabalhadas = input('Quantas horas trabalha por mês: ')
valor_hora = float(salario_mensal) / int(horas_trabalhadas)
print  (valor_hora)
