#067_ex_calculadora

while True:
    s_num_a = input('Digite o nro A: ')
    s_num_b = input('Digite o nro B: ')
    s_operador = input('Informe o Operador Aritmético (+ - / *): ')
    b_num_validos = None
    ...
    try:
        flo_a = float(s_num_a)
        flo_b = float(s_num_b)
        b_num_validos = True
    except:
        b_num_validos = None
    ...
    if b_num_validos is None:
        print('Um ou ambos os números são inválidos.')
        continue  #retorna para o while
    operadores_permitidos = '+-*/'
    if (s_operador not in operadores_permitidos) or len(s_operador) > 1:
        print('O Operador informado não é válido.')
        continue  #retorna para o while
    ...
    if s_operador == '+':
        print('A soma {0} + {1} = {2}'.format(flo_a, flo_b, (flo_a + flo_b)))
    if s_operador == '-':
        print('A subtração {0} - {1} = {2}'.format(flo_a, flo_b, (flo_a - flo_b)))
    if s_operador == '*':
        print('A multiplicação {0} * {1} = {2}'.format(flo_a, flo_b, (flo_a * flo_b)))
    if s_operador == '/':
        print('A divisão {0} / {1} = {2}'.format(flo_a, flo_b, (flo_a / flo_b)))
    ...
    sair = input('Quer sair? Digite [s] ou [sim]: ').lower().startswith('s')
    if sair is True:
        break