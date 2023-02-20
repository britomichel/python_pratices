# Trabalhar com Strings
meuString = "olá, meu Nome é Michel."
print( "meuString = "  + meuString )
print( "Trechos do meu 'array' [0]: "  + meuString[0] )
print( "Trechos do meu 'array' [3]: "  + meuString[3] )
print( "Trechos do meu 'array' [6]: "  + meuString[6] )
print( "Testar Função capitalize(): " + meuString.capitalize() )
print( "Testar Função upper(): " + meuString.upper() )
print( "Testar Função center(): " + meuString.center(50, "_") )
print( "Testar Função ljust(): " + meuString.ljust(30, "_") )
print( "Testar Função rjust(): " + meuString.rjust(30, "_") )
txt_nome = "Michel"
txt_numero = "22"
print( "Encontrar substring '" + txt_nome + "': posição = " + str(meuString.find(txt_nome)) )
print( "A variável txt_nome é número? " + str(txt_nome.isnumeric()) )
print( "A variável txt_numero é número? " + str(txt_numero.isnumeric()) )
print( "Tamanho do texto de '" + txt_nome + "'  = " + str(len(txt_nome)) )
print( "Tamanho do texto de '" + txt_numero + "'  = " + str(len(txt_numero)) )
print( "Trocar a palavra '" + txt_nome + "' por KANE: " + meuString.replace(txt_nome, "KANE") )
txt_bagunca = "   feijoada    "
print( "A string txt_bagunca tá com espaços a mais: '" + txt_bagunca + "'" )
print( "Remover espaços da esquerda: '" + txt_bagunca.lstrip() + "'" )
print( "Remover espaços da direita: '" + txt_bagunca.rstrip() + "'" )
print( "Remover espaços desnecessários: '" + txt_bagunca.strip() + "'" )
