class Palindromo:

  #palin = "SOCORRAM, ME SUBI NO ONIBUS EM MARROCOS!"
  palin = ""
  
  def __init__(self):
    self.palin

  def tirar_espacos(self):
    self.palin = self.palin.replace(" ","")
    return self.palin

  def tirar_virgulas(self):
    self.palin = self.palin.replace(",","")
    return self.palin

  def tirar_exclamação(self):
    self.palin = self.palin.replace("!","")
    return self.palin
  
  def lower_case(self):
    self.palin = self.palin.lower()
    return self.palin

  def padronizar():
    novo = Palindromo()
    palin = novo.tirar_espacos()
    palin = novo.tirar_virgulas()
    palin = novo.tirar_exclamação()
    palin = novo.lower_case()
    return palin

