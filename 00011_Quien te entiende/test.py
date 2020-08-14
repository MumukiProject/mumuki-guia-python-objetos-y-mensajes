# describe 'Interfaz de':
#   it 'Mercedes':
#     expect(interfaz_mercedes).to match_array ['cantar!']
#
#
#   it 'Pepita':
#     expect(interfaz_pepita).to match_array ['energia', 'cantar!', 'comer_lombriz!', 'volar_en_circulos!']
#
#
#   it 'Norita':
#     expect(interfaz_norita).to match_array ['cantar!', 'comer_lombriz!', 'volar_en_circulos!']

mayusminus="para Python, 'A' no es el mismo que 'a'."
interfaz_ejemplo="['mensaje1','mensaje2()']"


class Test(unittest.TestCase):

  def test_interfaz_de_Norita_tiene_todos_los_mensajes_que_entiende(self):
    interfaz_esperada=["cantar()","comer_lombriz()","volar_en_circulos()"]
    interfaz_entregada=interfaz_norita
    
    self.assertEqual(set(interfaz_esperada),set(interfaz_entregada),"la interfaz de {nombre} es algo como {iface}".format(nombre="Norita", iface=interfaz_ejemplo))

  def test_interfaz_de_Norita_con_palabras_en_minusculas(self):
    interfaz_esperada=["cantar()","comer_lombriz()","volar_en_circulos()"]    
    interfaz_entregada=interfaz_norita
    todos_minusculas=all([str(x).islower() for x in interfaz_entregada])
    self.assertTrue(todos_minusculas,mayusminus+" La interfaz de {nombre} tiene todas palabras en minúsculas (que pueden estar unidas por espacios subrayados), es algo como {iface}".format(nombre="Norita", iface=interfaz_ejemplo))

  def test_interfaz_de_Mercedes_tiene_todos_los_mensajes_que_entiende(self):
    interfaz_esperada=["energia","cantar()","comer_lombriz()","volar_en_circulos()"]
    interfaz_entregada=interfaz_mercedes
    
    self.assertEqual(set(interfaz_esperada),set(interfaz_entregada),"la interfaz de {nombre} es algo como {iface}".format(nombre="Mercedes", iface=interfaz_ejemplo))

  def test_interfaz_de_Mercedes_con_palabras_en_minusculas(self):
    interfaz_entregada=interfaz_mercedes
    todos_minusculas=all([str(x).islower() for x in interfaz_entregada])
    self.assertTrue(todos_minusculas,mayusminus+" La interfaz de {nombre} tiene todas palabras en minúsculas (que pueden estar unidas por espacios subrayados), es algo como {iface}".format(nombre="Mercedes", iface=interfaz_ejemplo))


  def test_interfaz_de_Mercedes_tiene_ambos_tipos_de_mensaje(self):
    interfaz_entregada=interfaz_mercedes
    ambos_tipos=any([not(str(x).endswith("()")) for x in interfaz_entregada])
    ambos_tipos&=any([str(x).endswith("()") for x in interfaz_entregada])
    self.assertTrue(ambos_tipos,"la interfaz de {nombre} tiene mensajes que terminan en (), y otros que no. como {iface}".format(nombre="Mercedes", iface=interfaz_ejemplo))
    

    