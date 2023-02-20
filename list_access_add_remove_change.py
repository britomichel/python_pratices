# list_access_add_remove_change

myList = ["Armando", "Bruno", "Cibele", "Denise", "Felipe", "Marcia"]
print("Lista ORIGINAL: ", myList)
print()

print("Segundo nome da lista (myList[1]):", myList[1])
print("Último nome da lista (myList[-1]):", myList[-1])
print("Do 2o em diante (myList[1:]): ", myList[1:])
print("Do 2o ao 5o nome (myList[1:4]): ", myList[1:4])
print("Os três primeiros (myList[:3]): ", myList[:3])
print("myList[-4:-1]: ", myList[-4:-1])

# verificar se existe e alterar
if "Cibele" in myList:
    print("Cibele encontra-se na lista.")
    print("Substituir Cibele por Camila.")
    myList[2] = "Camila"
else:
    print("Cibele não se encontra na lista.")

print("Lista ATUALIZADA (1): ", myList)

# atualizar um RANGE de elementos da lista
myList[3:6] = ["Dionísio", "Fausto", "Mytra"]
print("Lista ATUALIZADA (2): ", myList)

# inserir um RANGE de elementos no lugar de um elemento
print("myList[1:2]: ", myList[1:2])
myList[1:2] = ["Berlinda", "Bruna", "Carmem", "Celina"]
print("Lista ATUALIZADA (3): ", myList)

# substituir um RANGE de elementos por um único elemento
print("myList[3:6]: ", myList[3:6])
myList[3:6] = ["As Três Cezinhas"]
print("Lista ATUALIZADA (4): ", myList)

# inserir ítens na lista
print("Inserir 'Novinho' e 'Novinha' via .insert()")
myList.insert(2, "Novinho")
myList.insert(4, "Novinha")
print("Lista ATUALIZADA (5): ", myList)

# REMOVER um ÍTEM via remove()
print("Remover os ítens 'Novinho' e, depois, 'As Três Cezinhas' via .remove()")
myList.remove('Novinho')
myList.remove('As Três Cezinhas')
print("Lista ATUALIZADA (6): ", myList)

# append()
print("Adicionar via .append() o ítem 'Zuluzinho")
myList.append("Zuluzinho")
print("Lista ATUALIZADA (7): ", myList)

# Remover ítem via ÍNDICE
print("Remover ítem via ÍNDICE, ex.: .pop(1)")
myList.pop(1)
print("Lista ATUALIZADA (8): ", myList)

# Extender uma lista ou adicionar outra lista no final
myListAdicional = ["Níbia","Péricles", "Quênia", "Ryan"]
print("myListAdicional: ", myListAdicional)
myList.extend( myListAdicional )
print("myList EXTENDIDA 1: \n", myList)

# Extender uma lista ou adicionar outra lista no final
myTupleAdicional = ("Tibério", "Tristão", "Ulisses", "Venâncio")
print("myTupleAdicional: \n", myTupleAdicional)
myList.extend( myTupleAdicional )
print("myList EXTENDIDA 2: \n", myList)

# Remover o Último ítem da lista
myList.pop()
print("myList Removeu último: \n", myList)
myList.pop()
print("myList Removeu último novamente: \n", myList)

# Remover o Primeiro ítem da lista
del myList[0]
print("Removeu o Primeiro ítem da lista: \n", myList)
del myList[0]
print("Removeu o Primeiro ítem da lista novamente: \n", myList)

# Limpar dados da lista
myList.clear()
print("myList.clear(): ", myList)
print("Tam.: ", len(myList))

# Apagar todos o ítens da lista
del myList
print("del myList")
print("Não esixte mais myList, foi deletada")
