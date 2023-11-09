import unittest
from src.car import Car

class TestCar(unittest.TestCase):

    def setUp(self):
        # Create a car instance with some example attributes
        self.car = Car(make='TestMake', model='TestModel', mpg=25, tank_size=12, price=20000)

    def test_car_initialization(self):
        self.assertEqual(self.car.make, 'TestMake')
        self.assertEqual(self.car.model, 'TestModel')
        self.assertEqual(self.car.mpg, 25)
        self.assertEqual(self.car.tank_size, 12)
        self.assertEqual(self.car.price, 20000)

    def test_car_string_representation(self):
        # Assuming Car class has a __str__ method that returns a string
        self.assertEqual(str(self.car), 'TestMake TestModel')

if __name__ == '__main__':
    unittest.main()
