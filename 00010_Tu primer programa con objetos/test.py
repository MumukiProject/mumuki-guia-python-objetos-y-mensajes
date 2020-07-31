#...content...#

class Test(unittest.TestCase):
  def test_inspect(self):
    dir()
    self.assertTrue(False,dir(self))
    
    
  def test_inspect2(self):
    self.assertTrue(False,locals())
    
  