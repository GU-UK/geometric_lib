import math


def area(r):
    '''
    
    Вовращает площадь круга.

        Параметры:
            r (int): десятичное целое число.
            math.pi (float): десятичное число или число пи.

        Возвращаемое значение:
            math.pi * r * r (float): десятичное число.
        Пример:
        area(3)  =>  pi * 3 * 3 ~ 28,27433387
    '''
    return math.pi * r * r


def perimeter(r):
    '''

    Вовращает периметр круга.

        Параметры:
            r (int): десятичное целое число.
            math.pi (float): десятичное число или число пи.

        Возвращаемое значение:
            2 * math.pi * r (float): десятичное число.
        Пример:
        perimeter(3)  =>  2 * pi * 3 ~ 18,8495559
    '''
    return 2 * math.pi * r

import unittest
class CircleTestCase(unittest.TestCase):
    def test_area_circle(self):
        self.assertEqual(area(10), math.pi * 10 * 10)
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    def test_area_nointeger(self):
        res = area(9.3)
        self.assertAlmostEqual(res, 271.71634, places=4)

    def test_perimeter_circle(self):
        self.assertEqual(perimeter(10), 2 * math.pi * 10)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_1_non_integer(self):
        res = perimeter(9.3)
        self.assertAlmostEqual(res, 58.43362, places=4)
