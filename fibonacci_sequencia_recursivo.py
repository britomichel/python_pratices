#fibonacci_sequencia_recursivo
"""
    Autor: Michel Brito
    Descrição: Exibir a quantidade desejada de números 
    (elementos) da Sequência de Fibonacci.
"""
qtde = int(input('Informe a quantidade de números a serem gerados ' + \
                 'para a Sequência de Fibonacci: '))

def fibonacci_recursivo(n):
   if n <= 1:
       return n
   else:
       return fibonacci_recursivo(n - 2) + fibonacci_recursivo(n - 1)

print('Os {0} primeiros números da sequência de Fibonacci são:'.format(qtde), end = " ")

for i in range(qtde):
    print(fibonacci_recursivo(i), end = ' ')
