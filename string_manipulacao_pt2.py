#manipulação de String pt.2
#string check
txt1 = "The best thigs in life ar free."
txt2 = "We are the People. (via If...)"
txt3 = ""

txt3 = txt1 + " " + txt2
print( "Concatenação de txt1 e txt2: " + txt3 )

sFrase = "Meu nome é Kane, tenho {} anos de idade."
iIdade = 36
print(sFrase.format(iIdade) )

nroProduto = 912
decPreco = 19.95
iQtde = 5
nroPedido = 12982

# assim #
sPedido = "O Pedido nro.{} requer o produto {} na quantidade de {} pelo valor de  {} Reais. Grato."
print( sPedido.format(nroPedido, nroProduto, iQtde, decPreco) )

# ou #
sPedido = "Gostaria de adquidir o produto nro. {1} pelo valor de {3} reais a partir da quantidade de {2} peças. Grato"
print( sPedido.format(nroPedido, nroProduto, iQtde, decPreco) )
