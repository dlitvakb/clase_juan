import unittest
from ambulancia import Ambulancia, EstadoEnTransito

class TestAmbulancia(unittest.TestCase):
    def test_ambulancia_esta_disponible_por_default(self):
        ambulancia = Ambulancia()
        self.assertTrue(ambulancia.esta_disponible())

    def test_ambulancia_con_otro_estado_no_esta_disponible(self):
        ambulancia = Ambulancia(EstadoEnTransito())
        self.assertFalse(ambulancia.esta_disponible())

if __name__ == '__main__':
    unittest.main()