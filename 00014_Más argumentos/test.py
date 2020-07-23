class Test(unittest.TestCase):

    def test_Pepita_quedó_en_la_ciudad_correcta(self):
        Pepita = pajaritoClass("Pepita")
        Pepita.comer_alpiste(500)
        Pepita.volar_hacia(Iruya)
        Pepita.volar_hacia(Oberá)
        result = "Oberá"
        self.assertEqual(result, Oberá.nombre, " la ciudad debería ser '{}' ".format(result))
        pass

    def test_Pepita_quedó_con_energia_correcta(self):
        Pepita = pajaritoClass("Pepita")
        Pepita.comer_alpiste(500)
        Pepita.volar_hacia(Iruya)
        Pepita.volar_hacia(Oberá)
        result = 500 * 15 - Oberá.distancia_con(Iruya) * 3
        self.assertEqual(result, Pepita.energia, " la energía residual debería ser {} ".format(result))
        pass