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
class Test(unittest.TestCase):

  def test_interfaz_de_Norita_tiene_todos_los_mensajes(self):
    interfaz_esperada=["energia","cantar()","comer_lombriz()","volar_en_circulos()"]
    interfaz_entregada=interfaz_norita
    
    self.assertEqual(set(interfaz_esperada),set(interfaz_entregada),"la interfaz de {nombre} es algo como {iface}".format(nombre="Norita", iface=str(interfaz_esperada[:2])))

  def test_interfaz_de_Norita_con_minusculas(self):
    interfaz_entregada=interfaz_norita
    todos_minusculas=all([str(x).islower() for x in interfaz_entregada])
    self.assertTrue(todos_minusculas,"la interfaz de {nombre} tiene todas palabras en minúsculas (que pueden estar unidas por espacios subrayados), es algo como {iface}".format(nombre="Norita", iface=str(interfaz_esperada[:2])))
