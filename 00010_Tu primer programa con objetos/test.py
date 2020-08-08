class Test(unittest.TestCase):
    def test_Pepita_quedó_con_energia_correcta(self):
        result = Pepita.energia
        self.assertEqual(result, 150,"El mensaje `Pepita.energia` devolvió {} y debería devolver 150.\n En otras: palabras el atributo `energía` de Pepita no tiene el valor pedido".format(result))