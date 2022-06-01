from palindromo import Palindromo

def test_minimum():
  assert Palindromo.palindromo("")

def test_maximum():
   assert Palindromo.palindromo("SOCORRAM ME SUBI NO ONIBUS EM MARROCOS"*50)

def test_size_ok():
     assert Palindromo.palindromo("SOCORRAM ME SUBI NO ONIBUS EM MARROCOS")

def test_no_palindromo():
  assert Palindromo.palindromo("Daniel")

def test_palindromo():
     assert Palindromo.palindromo("ovo")

def test_no_string():
  assert Palindromo.palindromo("Daniel123")

