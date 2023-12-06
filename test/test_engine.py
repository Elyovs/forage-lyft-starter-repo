import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        current_milleage = 60000
        last_service_milleage = 30000
        engine = CapuletEngine(current_milleage, last_service_milleage)

        self.assertFalse(engine.needs_service())
    
    def test_engine_should_be_serviced(self):
        current_milleage = 60001
        last_service_milleage = 30000
        engine = CapuletEngine(current_milleage, last_service_milleage)

        self.assertTrue(engine.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        warning_light = False
        engine = SternmanEngine(warning_light)

        self.assertFalse(engine.needs_service())
    
    def test_engine_should_be_serviced(self):
        warning_light = True
        engine = SternmanEngine(warning_light)

        self.assertTrue(engine.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_not_be_serviced(self):
        current_milleage = 120000
        last_service_milleage = 60000
        engine = WilloughbyEngine(current_milleage, last_service_milleage)

        self.assertFalse(engine.needs_service())
    
    def test_engine_should_be_serviced(self):
        current_milleage = 120001
        last_service_milleage = 60000
        engine = WilloughbyEngine(current_milleage, last_service_milleage)

        self.assertTrue(engine.needs_service())