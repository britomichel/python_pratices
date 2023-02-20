#manipulação de String pt.1
#string check
txt = "The best thigs in life ar free."
print("Frase Orig.: " + txt)
print("free" in txt)
print("Existe 'free' na frase? " + str("free" in txt))

txt = "We are the People. (via If...)"
print("Frase Orig.: " + txt)

if "people" in txt:
    print("Yes, 'people' is present.")

print("NOT IN")
if "monsters" not in txt:
    print("No, 'monsters' is not present.")

#pegar um trecho da String
print("Frase Original: " + txt)
print( "txt[10:16] => " + txt[10:17] )
print( "txt[:6] => " + txt[:6] )
print( "txt[7:] => " + txt[7:] )
print( "txt[-10:-16] => " + txt[-19:-13] )

print()
print( "txt.upper() => " + txt.upper() )
print( "txt.lower() => " + txt.lower() )

print()

sEspacos = "    espaços antes e depois     "
print("Original: '" + sEspacos + "'")
print(".strip() => '" + sEspacos.strip() + "'")

print()
print( ".replace(a, b) => " + txt.replace("People", "Aliens") )

sPalavras = "banana, pêra, laranja, melão, kiwi"
arrFrutas = sPalavras.split(",")
print("Original: " + sPalavras )
print( arrFrutas )
print("arrFrutas[2] = " + arrFrutas[2])
