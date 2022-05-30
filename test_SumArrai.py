
arrai = [0,1,4,15]

def test_size_minimum():
  if len(arrai) > 0:
    resul = True
  else:
    resul = False

  assert resul

def test_size_maximum():
  if len(arrai) <= 1000:
    resul = True
  else:
    resul = False

  assert resul

def test_type_arrai():
  for x in range(len(arrai)):
    if not type(arrai[x]) is int:
      resul = False
    else: 
      resul = True
    assert resul

def test_TypeSoma():
  cr = 0

  for x in range(len(arrai)):
    try:
      cr += arrai[x]
    except:
      print("valores com tipos diferentes do esperado")
  assert type(cr) is int 