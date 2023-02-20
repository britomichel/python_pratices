#boolean_tests
print("10 > 9: ", 10 > 9)
print("10 == 9: ", 10 == 9)
print("10 < 9: ", 10 < 9)
print("bool('Hello'): ", bool('Hello'))
print("bool(''): ", bool(''))
print("bool(100): ", bool(100))
print("bool(0): ", bool(0))
arFull = ["apple", "cherry", "banana"]
arEmpty = []
print("bool(arFull): ", bool(arFull))
print("bool(arEmpty): ", bool(arEmpty))
print()

a = 200
b = 33

if b > a:
    print("b é maior que a")
else:
    print("b não é maior que a")

print("...ou...")

resp = "O valor de b ({1}) {2} é maior que o valor de a ({0})\n"
if a > b:
    print( resp.format(a, b, "NÃO") )
else:
    print( resp.format(a, b, "") )

x = 2.19
print("isinstance(a, int): ", isinstance(a, int))
print("isinstance(x, int): ", isinstance(x, int), "\n")

def funcSimOuNao(sim_ou_nao) :
    if (sim_ou_nao.lower() == 'sim') :
        return True
    else :
        return False

print( "funcSimOuNao('sim'): ", funcSimOuNao('sim') )
print( "funcSimOuNao('não'): ", funcSimOuNao('não') )
