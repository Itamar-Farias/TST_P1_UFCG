import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
pivot = getattr(undertest, 'pivot', None)

class PublicTests(unittest.TestCase):

    def test_exemplo_1(self):
        numeros = [6, 4, 8, 1, 7, 3]
        pivot(numeros)
        assert numeros == [4, 1, 3, 6, 8, 7], numeros
        


if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
