import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
inverte_dicionario = getattr(undertest, 'inverte_dicionario', None)

class PublicTests(unittest.TestCase):

    def test_exemplo(self):
        m = {"a": 2, "b": 3, "c": 2}
        assert inverte_dicionario(m) == {
          2: ["a", "c"],
          3: ["b"]
        }

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
