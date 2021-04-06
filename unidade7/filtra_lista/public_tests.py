import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
filtra_altera_lista = getattr(undertest, 'filtra_altera_lista', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
       seq = [0,1,2,3,4,5,6]
       filtra_altera_lista(2, seq)
       assert seq == [0, 2, 4 ,6]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
