#fibonacci_sequencia
"""
    Autor: Michel Brito
    Descrição: Exibir a quantidade desejada de números 
    (elementos) da Sequência de Fibonacci.
"""

qtde = int( input('Informe a quantidade de números que' + \
             'deseja gerar para a Seqência de Fibonacci: ') )
a = -1
b = 1
soma = 0

resp = 'Os {} primeiros números da sequência de Fibonacci são:'.format(qtde)
for i in range(qtde):
    soma = a + b
    a = b
    b = soma
    print ('Elemento {}: {}'.format(i+1, soma))
