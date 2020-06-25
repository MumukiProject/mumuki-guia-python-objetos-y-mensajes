

  def test_haber_perdido_energia(self):
    """haber perdido energía"""
    self.assertEqual(Pepita.energia,3580)
    
  def test_estar_en_Obera(self):
    """estar en Oberá"""
    self.assertTrue(isInstance(Pepita.ciudad,Obera))
