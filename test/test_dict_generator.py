import unittest
from RandomListOrDictGenerator.list_or_dict_generator import RandomListOrDictionnary
  
class DictGeneratorTest(unittest.TestCase):
  
    def setUp(self):
        self.size = 5
        self.clss = RandomListOrDictionnary(size=self.size, key_length=3, values_length=5)
        self.dic = self.clss.createRandomDictionnary()
    
    def test_test(self):        
        self.assertTrue(len(self.dic)==self.size)
  
if __name__ == '__main__':
    unittest.main()