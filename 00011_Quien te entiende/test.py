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

  def test_interfaz_de_Norita(self):
    interfaz_esperada=["cantar()","comer_lombriz()","energia","volar_en_circulos()"]
    interfaz_entregada=interfaz_norita
    
    self.assertEqual(set(interfaz_esperada),set(interfaz_entregada),"la interfaz de {nombre} es algo como {iface}".format(nombre="Mercedes", iface=str(interfaz_esperada)))
