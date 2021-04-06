import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
quem_bebeu_mais_menos = getattr(undertest, 'quem_bebeu_mais_menos', None)

class PublicTests(unittest.TestCase):

    def test_1(self):
        sabado = [[1,2,3], [0,1,0], [3,1,2]]
        domingo = [[2,1,3], [0,2,1], [1,1,2]]
        assert quem_bebeu_mais_menos(sabado, domingo) == (3,1)
        
    def test_2(self):
        sabado = [[1,2,3,4,5], [0,1,2,3,1], [2,1,0,1,2], [3,1,2,1,3], [4,1,3,0,0]]
        domingo = [[0,1,1,0,1], [1,2,2,0,2], [2,3,1,1,1], [3,4,2,0,0], [4,3,3,0,0]]
        assert quem_bebeu_mais_menos(sabado, domingo) == (1,4)
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
