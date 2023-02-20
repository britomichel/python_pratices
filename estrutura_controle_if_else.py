nome = input("Qual é o seu nome? \n") 
if nome == "Michel": 
    print("Conheço o %s" % nome)
else:
    print("Não conheço essa pessoa!")

curso = input("Qual é o seu curso (Matemática, Português, Ciências, Outros)? \n") 
if curso == "Matemática": 
    print("O curso %s se inicia em Janeiro" % curso)
elif curso == "Português": 
    print("O curso %s se inicia em Fevereiro" % curso)
elif curso == "Ciências": 
    print("O curso %s se inicia em Março" % curso)
else:
    print("O curso %s ainda não tem data para inicio. Consulte mais tarde." % curso)
