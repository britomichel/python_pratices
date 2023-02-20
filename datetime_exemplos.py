# importando o módulo datetime
from datetime import date
data1 = date(2016, 12, 9)
print( "data1 = " + str(data1))
print( "data atual: " + str(date.today()) )

# ex.2.
hoje = date.today()
data2 = date(hoje.year, hoje.month, 1) 
print( "O primeiro dia do mês é: " + str(data2) )

# diferença entre datas
carnaval_2023 = date(2023, 2, 24) 
tempo_para_o_carnaval = abs(carnaval_2023 - date.today())
print( "Dias que faltam para o carnaval de 2023: " + str(tempo_para_o_carnaval.days) )

# ex.
print( "Dia da semana = " + str(hoje.weekday()) ) 
data2 = data2.replace(day=5) 
print( "5o. dia do mês: " + str(data2) )

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# TEMPO, Horas, minutos, segundos, frações de segundos
from datetime import time

# Ex.1
tempo1 = time(12, 25, 31, 1333) 
print( tempo1 )
print( tempo1.strftime("%H horas, %M minutos e %S segundos") )

# Ex.2
datatempo1 = time(10, 10, 18, 1444)
print( "Horário informado: " + str(datatempo1) ) 

datatempo2 = time()
print( "Horário atual: " + str(datatempo2) )
