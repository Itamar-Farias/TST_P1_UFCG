import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
inverte2a2 = getattr(undertest, 'inverte2a2', None)

class PublicTests(unittest.TestCase):

   def test_basico(self):
       seq = [10,20,30,40,50,60]
       inverte2a2(seq)
       assert seq == [20,10,40,30,60,50]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
