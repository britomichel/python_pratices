# list_loop_members_or_index

myList = ["Arth", "Biah", "Joshua", "Mirla", "Paulo", "Giorgio"]

for sNome in myList:
    print("Nome:", sNome)

iTamanho = len(myList)
for i in range( iTamanho ):
    print( i, "->", myList[i] )

i = 0
while i < iTamanho:
    print( "índice {0}, valor: {1}".format(i, myList[i]) )
    i += 1

# Utilizando List Comprehension
[print(sNome) for sNome in myList]
