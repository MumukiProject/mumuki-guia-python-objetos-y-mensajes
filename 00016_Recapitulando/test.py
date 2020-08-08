class Test(unittest.TestCase):
  def test_Pepita_quedó_en_la_ciudad_correcta(self):
    # describe 'Pepita':
    #  before(:each) { Pepita.volar_hacia!(Oberá) }
    #  it 'vuela a Iruya':
    result = Pepita.ciudad
    self.assertEqual(result, Ushuaia, " la ciudad final debería ser '{}' ".format(Ushuaia))
    pass
  
  def test_Pepita_pasó_por_Iruya(self):
    # describe 'Pepita':
    #  before(:each) { Pepita.volar_hacia!(Oberá) }
    #  it 'vuela a Iruya':
    ciudad_importante = Iruya
    itinerario = Pepita.ciudades_anteriores
    result = any(ciudad_visitada == ciudad_importante for ciudad_visitada in itinerario)
    result= str([ciudad_visitada.nombre  for ciudad_visitada in itinerario])
    self.assertTrue(result=="",
                    " Iruya es una ciudad importante y debería  ser parte del itinerario ({})".format(resut))
    pass
  
  def test_Pepita_quedó_con_energia_correcta(self):
    """ 1. Coma 90 gramos de alpiste. :rice:
        > 1. Vuele a Iruya. :earth_americas:
        > 1. Finalmente, coma tanto alpiste como el 10% de la energía que le haya quedado"""
    result = 850
    result = -73385 #lo qué???
    self.assertEqual(result, Pepita.energia, " la energía residual debería ser {} ".format(result))
    pass
  #
  #  it 'termina con 850 de energía cuando empieza con 1000':
  #    Pepita.energia = 1000
  #
  #    #...content...#
  #
  #    expect(Pepita.energia).to eq 850
  #
  #
  #  it 'termina con 100 cuando empieza con 700':
  #    Pepita.energia = 700
  #
  #    #...content...#
  #
  #    expect(Pepita.energia).to eq 100
  #