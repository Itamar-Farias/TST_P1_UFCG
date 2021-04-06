import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
move_impostor = getattr(undertest, 'move_impostor', None)

class PublicTests(unittest.TestCase):

   def test_exemplo(self):
       lista = [1,2,4,3,5,8]
       assert move_impostor(lista) == None
       assert lista == [1,2,3,4,5,8]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))

lista = [1,2,4,3,9,8]
assert move_impostor(lista) == None
assert lista == [1,2,3,4,9,8]
