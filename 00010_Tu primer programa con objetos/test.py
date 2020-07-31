#...extra...#
def test_00010_Pepita_quedó_con_energia_correcta(self):
  #Pepita = pajaritoClass("Pepita")
  #for _ in range(8):
  #      Pepita. comer_lombriz()  #+20
  #Pepita.volar_en_circulos()  # -10
  result = 150
  self.assertEqual(result, Pepita.energia, "El mensaje `Pepita.energia` debería devolver `{}`. En otras: palabras el atributo 'energía' de Pepita no tiene el valor pedido ".format(result))
  pass