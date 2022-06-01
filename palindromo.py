class Palindromo:
  
  def __init__(self,palin):
    self.palin = palin

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

  def size_limit(self):
    if (len(self.palin) <= 1000):
      return True
    return False

  def size_minimum(self):
    if len(self.palin) > 0:
      return True
    return False

  def check_palindromo(self):

    n = len(self.palin)
    j = n-1

    for x in range(n):
      if self.palin[x] != self.palin[j]:
        return False
      j-=1
    return True
    
  def palindromo(palin):
    novo = Palindromo(palin)
    palin = novo.tirar_espacos()
    palin = novo.tirar_virgulas()
    palin = novo.tirar_exclamação
    palin = novo.lower_case()
    if novo.size_limit() and novo.size_minimum() and novo.check_palindromo():
      return True
    
    return False