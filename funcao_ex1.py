# define a FUNÇÃO
def print_varias_vezes():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
      print(x)

def my_function(fname):
  print("Sr(a). " + fname)

def numero_ao_cubo(numero): 
    valor_a_retornar = numero * numero * numero
    return(valor_a_retornar)

def print_tudo_2_vezes(*args): 
    for parametro in args: 
        print(parametro + "! " + parametro + "!")

def print_info(**kwargs): 
    for parametro, valor in kwargs.items(): 
        print( parametro + " - " + str(valor) )

# invoca a FUNÇÃO print_varias_vezes()
print("Vai executar a função...")
print_varias_vezes()

# invoca a FUNÇÃO my_function(fname)
my_function("Michel")
my_function("Cibelle")
my_function("Lorena")

# invoca a FUNÇÃO numero_ao_cubo(numero)
resposta = numero_ao_cubo( float( input("Digite um número para Elevar ao Cubo: ") ) )
print( str(resposta) )

# Função com vários argumentos
print_tudo_2_vezes("Olá", "Python", "Felipe", "Choroquina")

# invoca a Função que utiliza DICIONÁRIO
print_info( nome="Felipe", idade=30, nacionalidade="Brasil" )
print_info( cidade="Jundiaí", profissao="Analista Programador", salario=4500 )
