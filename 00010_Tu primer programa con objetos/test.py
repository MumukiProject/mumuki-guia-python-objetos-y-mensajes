

class Test(unittest.TestCase):
  def test_inspect(self):
    self.assertTrue(False,dir(self))
    
  def test_inspect2(self):
    self.assertTrue(False,locals())
    
  