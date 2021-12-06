import unittest

from day_12 import Moon

class TestMoon(unittest.TestCase):
    moon = Moon([1, 0, 2], "Io")
    print(moon)
    moon.velocity = [0,0,0]
    
    def test_calculate_gravity(self):
        moon = Moon([1, 0, 2], "Io")
        print("eeee", list(map(moon.calculate_gravity(), [-1,0,2], [2,-10,-7])))

    def test_velocity(self):
        moon = Moon([1, 0, 2], "Io")
        moon.apply_velocity([2,1,-1])
        print(moon.velocity)

    #def test_calculate_gravity(self):
    #    moon = Moon([1, 0, 2], "Io")
    #    print(moon.calculate_gravity(-3,5))



