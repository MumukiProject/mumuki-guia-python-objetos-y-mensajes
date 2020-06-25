class tests(unittest):
  def test_haber_perdido_energia(self):
    """haber perdido energía"""
    assertEqual(Pepita.energia,3580)
    
  def test_estar_en_Obera(self):
    """estar en Oberá"""
    assertTrue(isInstance(Pepita.ciudad,Obera))
    
    
    