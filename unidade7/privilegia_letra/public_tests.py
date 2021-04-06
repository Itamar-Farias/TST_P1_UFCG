import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
letra_magica = getattr(undertest, 'letra_magica', None)

class PublicTests(unittest.TestCase):

   def test_adicional_1(self):
        fila = ["carlos", "bruno", "andre", "daniel", "ana", "carla"]
        letra_magica(fila, "a")
        assert fila == ["andre", "ana", "carlos", "bruno", "daniel", "carla"]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
