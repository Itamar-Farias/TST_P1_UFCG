import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
insere_na_fila = getattr(undertest, 'insere_na_fila', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):

        fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]
        insere_na_fila(fila, "jose", 1.12)
        assert fila == [("maria", 1.05), ("joao", 1.09), ("jose", 1.12), ("ana", 1.16)], fila

    def test_variacao_exemplo(self):

        fila = [("andre", 1.15), ("daniel", 1.19), ("carlos", 1.26)]
        insere_na_fila(fila, "marcos", 1.17)
        assert fila == [("andre", 1.15), ("marcos", 1.17), ("daniel", 1.19), ("carlos", 1.26)], fila



if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
