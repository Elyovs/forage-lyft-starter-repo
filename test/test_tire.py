import unittest

from tire.carrigan_tire import Carrigan
from tire.octoprime_tire import Octoprime

class TestCarrigan(unittest.TestCase):
    def tire_should_not_be_serviced(self):
        tire1 = 0.5
        tire2 = 0.8
        tire3 = 0.7
        tire4 = 0.2
        tire_arr = [tire1, tire2, tire3, tire4]
        tires = Carrigan(tire_arr)
        
        self.assertFalse(tires)

    def tire_should_be_serviced(self):
        tire1 = 0.5
        tire2 = 0.8
        tire3 = 0.9
        tire4 = 0.2
        tire_arr = [tire1, tire2, tire3, tire4]
        tires = Carrigan(tire_arr)
        
        self.assertTrue(tires)

class TestOctoprime(unittest.TestCase):
    def tire_should_not_be_serviced(self):
        tire1 = 0.5
        tire2 = 0.8
        tire3 = 0.7
        tire4 = 0.2
        tire_arr = [tire1, tire2, tire3, tire4]
        tires = Octoprime(tire_arr)
        
        self.assertFalse(tires)

    def tire_should_be_serviced(self):
        tire1 = 0.6
        tire2 = 0.8
        tire3 = 0.9
        tire4 = 0.7
        tire_arr = [tire1, tire2, tire3, tire4]
        tires = Octoprime(tire_arr)
        
        self.assertTrue(tires)