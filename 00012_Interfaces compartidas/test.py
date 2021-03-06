# describe 'Interfaz compartida entre':
#   it 'Mercedes y Norita':
#     expect(interfaz_compartida_entre_mercedes_y_norita).to match_array ['cantar!']
#
#
#   it 'Pepita y Norita':
#     expect(interfaz_compartida_entre_pepita_y_norita).to match_array ['cantar!',  'comer_lombriz!', 'volar_en_circulos!']
#
#
#   it 'todas':
#     expect(interfaz_compartida_entre_todas).to match_array ['cantar!']
interfaz_ejemplo="['mensaje1','mensaje2()']"



class Test(unittest.TestCase):

  def test_interfaz_compartida_entre_mercedes_y_norita(self):
    interfaz_esperada=["cantar()"]
    interfaz_entregada=interfaz_compartida_entre_mercedes_y_norita 
    
    self.assertEqual(set(interfaz_esperada),set(interfaz_entregada),"la interfaz compartida entre {nombre} es algo como {iface}".format(nombre="Mercedes y Norita", iface=interfaz_ejemplo))


  def test_interfaz_compartida_entre_todas(self):
    interfaz_esperada=["cantar()"]
    interfaz_entregada=interfaz_compartida_entre_todas
    self.assertEqual(set(interfaz_esperada),set(interfaz_entregada),"la interfaz compartida entre {nombre} es algo como {iface}".format(nombre="todos los objetos", iface=interfaz_ejemplo))


  def test_interfaz_compartida_entre_pepita_y_norita(self):
    interfaz_esperada=["cantar()","comer_lombriz()","volar_en_circulos()"]
    interfaz_entregada=interfaz_compartida_entre_pepita_y_norita
    
    self.assertEqual(set(interfaz_esperada),set(interfaz_entregada),"la interfaz compartida entre {nombre} es algo como {iface}".format(nombre="Pepita y Norita", iface=interfaz_ejemplo))
