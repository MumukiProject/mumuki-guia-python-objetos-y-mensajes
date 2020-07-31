class Test(unittest.TestCase):
  def test_inspect(self):
    self.assertTrue(False,str(dir()))
    
  def test_inspect2(self):
    self.assertTrue(False,str(locals()))