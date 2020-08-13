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
    interfaz_esperada=set(["cantar()","comer_lombriz()","energia","volar_en_circulos()"])
    interfaz_entregada=set(interfaz_norita)
    
    self.assertEqual(interfaz_pepita,interfaz_entregada)
