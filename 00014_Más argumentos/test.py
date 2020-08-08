class Test(unittest.TestCase):

    def test_Pepita_quedó_en_la_ciudad_correcta(self):
        result = Pepita.ciudad
        self.assertEqual(result, Oberá, " la ciudad debería ser '{}' ".format(result))
        pass

    def test_Pepita_quedó_con_energia_correcta(self):
        result = 100 + 500 * 15 - Oberá.distancia_con(Iruya) * 3
        self.assertEqual(result, Pepita.energia, " la energía residual debería ser {} ".format(result))
        pass