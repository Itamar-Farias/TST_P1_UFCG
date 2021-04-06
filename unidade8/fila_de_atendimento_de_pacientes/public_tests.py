import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
filas_de_atendimento = getattr(undertest, 'filas_de_atendimento', None)

class PublicTests(unittest.TestCase):

    def test_exemplo1(self):
        fila_unica = [ 'Andre', 'Antonio', 'Bianca', 'Carlos', 'Claudia']
        assert filas_de_atendimento(fila_unica, 3) == [['Andre','Carlos'],['Antonio', 'Claudia'], ['Bianca']]        

    def test_exemplo2(self):
        fila_unica = ['Andre', 'Antonio', 'Bianca', 'Carlos']
        assert filas_de_atendimento(fila_unica, 2) == [['Andre','Bianca'],['Antonio', 'Carlos']]

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
