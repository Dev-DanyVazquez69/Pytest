class Sum_array:

    def __init__(self,arrai):
        self.self.arrai = arrai

    def test_size_minimum(self):
        if len(self.arrai) > 0:
            resul = True
        else:
            resul = False

    def test_size_maximum(self):
        if len(self.arrai) <= 1000:
            resul = True
        else:
            resul = False


    def test_type_arrai(self):
        for x in range(len(self.arrai)):
            if not type(self.arrai[x]) is int:
                resul = False
            else: 
                resul = True
        assert resul

    def test_TypeSoma(self):
        cr = 0

        for x in range(len(self.arrai)):
            try:
                cr += self.arrai[x]
            except:
                print("valores com tipos diferentes do esperado")

    def index(arrai):
        novo = Sum_array
        if novo.test_size_maximum() and novo.test_size_minimum() and novo.test_type_arrai():
            return True
        return False