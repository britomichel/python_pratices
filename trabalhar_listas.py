# Trabalhar com listas
lis_alunos = ["Arnaldo", "Beatriz", "Carlos"]
lis_notas = [8.5, 9.2, 6.7]
lis_vazia = []
lis_mistura = ["XYZ", 9.9, "bateria", 6]
print( lis_alunos )
print( lis_notas )
print( lis_vazia )
print( lis_mistura )
print( " \n" )

# tamanho da lista
print( "tamano de lis_alunos = " + str(len( lis_alunos )) )
print( "tamano de lis_notas = " + str(len( lis_notas )) )

# acessar pelo índice
int_indice = 0
print( "Aluno nro. " + str(int_indice) + ": " + lis_alunos[int_indice] )
print( "Nota = " + str( lis_notas[int_indice] ) + " \n" )
int_indice = 1
print( "Aluno nro. " + str(int_indice) + ": " + lis_alunos[int_indice] )
print( "Nota = " + str( lis_notas[int_indice] )  + " \n" )

# alterar valores nas listas
print( "Notas Antes:" )
print( lis_notas )
lis_notas[0] = 9.0
lis_notas[2] = 6.5
print( "Notas Depois:" )
print( lis_notas )

# incluir ítens nas listas
# append
lis_alunos.append( "Cibelle" )
lis_notas.append( 10.0 )
print( lis_alunos )
print( lis_notas )
# insert
lis_alunos.insert(1, "Michel")
lis_notas.insert(1, 9.8)
print( lis_alunos )
print( lis_notas )

# tamanho da lista
print( "tamano de lis_alunos = " + str(len( lis_alunos )) )
print( "tamano de lis_notas = " + str(len( lis_notas )) )

# extend
lis_novos_nomes = ["Alice", "Bella"]
lis_novos_notas = [9.9, 8.8]
lis_alunos.extend( lis_novos_nomes )
lis_notas.extend( lis_novos_notas )
print( lis_alunos )
print( lis_notas )

# tamanho da lista
print( "tamano de lis_alunos = " + str(len( lis_alunos )) )
print( "tamano de lis_notas = " + str(len( lis_notas )) )

# remover ítens
lis_alunos.pop(2)  #remove conforme o índice
lis_notas.pop(2)   #remove conforme o índice
lis_alunos.pop()   #remove o último
lis_notas.pop()    #remove a última
print( lis_alunos )
print( lis_notas )

# Informações da LISTA
print( "tamano de lis_alunos = " + str(len( lis_alunos )) )
print( "tamano de lis_notas = " + str(len( lis_notas )) )
print( "maior nota  = " + str(max( lis_notas )) )
print( "menor nota  = " + str(min( lis_notas )) )

# Dicionário
dic_alunos = { "nome" : "Kane", "idade" : 49, "cidade" : "São Paulo" }
print( dic_alunos )
print( "O nome do aluno é: " + dic_alunos["nome"] )
print( "A idade do aluno é: " + str(dic_alunos["idade"]) )
print( "A cidade do aluno é: " + dic_alunos["cidade"] )
