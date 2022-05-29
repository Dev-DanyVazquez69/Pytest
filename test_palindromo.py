#arquivo de testes para o desafio de palindrom
from palindromo import Palindromo
import pytest

palin = Palindromo.padronizar()

#testar minimo de caracteres 
def test_size_minimum():
  if len(palin) > 0:
    resul = True
  else:
    resul = False

  assert resul

#testar maximo de caracteres
def test_size_limit():
  if len(palin) <= 1000:
    resul = True
  else:
    resul = False

  assert resul

#testar se é um Palindromo verificando se a ultima letra é igual a primeira podendo definir um palindromo
def test_End_Start():
  if (palin[0]) == (palin[-1]):
    resul = True
  else:
    resul = False

  assert resul

#verificar se o texto inverso é igual ao normal(palindromo) 
def test_verificar_oposto():
  palin_reverse = ''.join(reversed(palin))
  assert palin_reverse == palin