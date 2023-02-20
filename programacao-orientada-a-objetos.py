# o. o. p.
# Programação Orientada a Objetos

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# CLASSE
# Definindo nossa primeira CLASSE - Definição: def __init__(self)
# *O nome inicia com Letra Maiúscula. Ex.: 'Usuario'
class Usuario:
  contador = 0

  # Definições - - - - - - - - -
  def __init__(self, nome, email):
    self.nome = nome
    self.email = email
    Usuario.contador += 1

  # Funções - - - - - - - - -
  def diga_ola(self):
    print("Olá (qtd.'%s'), meu nome é %s e meu email é %s" % (str(self.contador), self.nome, self.email))

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# Criando o primeiro OBJETO da classe
print( "criar objeto usuario1..." )
usuario1 = Usuario(nome="Felipe", email="contato@felipegalvao.com.br")

usuario1.diga_ola()
print( "usuario1, contador = " + str(Usuario.contador) )

print(usuario1.nome)

# Alterando propriedade do objeto
usuario1.nome = "Felipe Galvão"
print(usuario1.nome)

# Funções para alterar, recuperar e deletar uma propriedade
print( "propriedades do objeto usuario1... (hasattr e getattr)" )

print( hasattr(usuario1, "nome") )
print( hasattr(usuario1, "idade") )
print( getattr(usuario1, "email") )

# Alterar propriedades
print( "Alterar propriedades de usuario1..." )
setattr(usuario1, "nome", "Felipe G.")
setattr(usuario1, "idade", 30)

print( "getattr nome = " + getattr(usuario1, "nome") )
print( "getattr idade = " + str(getattr(usuario1, "idade")) )

# Deletar uma propriedade do usuario1
delattr(usuario1, "idade")
usuario1.diga_ola()
# print(getattr(usuario1, "idade"))

# Variável de classe - contador
# criar outro OBJETO utilizando a Classe 'Usuario'
usuario2 = Usuario(nome="Jurema", email="jurema@jurema.com")
usuario2.diga_ola()
print( "usuario2, contador = " + str(Usuario.contador) )

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# HERANÇA de CLASSE - Definição de uma classe estendida a partir de outra classe
# Usuario / Administrador
class Administrador(Usuario):
  
  # Funções - - - - - - - - -
  def __init__(self, nome, email, chave_de_administrador):
    Usuario.__init__(self, nome, email)
    self.chave_de_administrador = chave_de_administrador


  def poder_administrativo(self):
    print("Eu tenho o poder! Minha chave é %s" % self.chave_de_administrador)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

usuario_adm = Administrador(nome="Admin", email="admin@admin.com", chave_de_administrador="123456")
usuario_adm.diga_ola()
print( "usuario_adm, contador = " + str(usuario_adm.contador) )
usuario_adm.poder_administrativo()

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =

# NOVA CLASSE, sobrescrevendo o método diga_ola da classe original
class MembroStaff(Usuario):
  
  # Funções
  def __init__(self, nome, email):
    Usuario.__init__(self, nome, email)

  # Sobrescrevendo o Método diga_ola(self) da Classe Usuario
  def diga_ola(self):
    print("Olá, meu nome é %s e eu sou membro do Staff. Em que posso ajudar?" % (self.nome))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

membro_staff_1 = MembroStaff(nome="Mariazinha", email="maria@zinha.com.br")
membro_staff_1.diga_ola()
