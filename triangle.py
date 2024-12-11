def area(a, h):
    '''
    Вовращает площадь треугольника.

        Параметры:
            a (int): десятичное целое число.
            h (int): десятичное целое число.

        Возвращаемое значение:
            a * h / 2 (float): десятичное число.
        Пример:
        area(2, 3)  =>  a * h / 2 = 3
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Вовращает периметр треугольника.

        Параметры:
            a (int): десятичное целое число.
            b (int): десятичное целое число.
            c (int): десятичное целое число.

        Возвращаемое значение:
            a + b + c (int): десятичное целое число.
        Пример:
        perimeter(1, 2, 3)  =>  a + b + c = 6
    '''
    return a + b + c

import unittest
class circleqweqwe(unittest.TestCase):
    def test_area_triangle(self):
        self.assertEqual(area(10, 5), 25)
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
    def test_area_neg(self):
        x, y = -5, -12
        self.assertEqual(area(x, y), 30)

    def test_perimeter_triangle(self):
        self.assertEqual(perimeter(10, 5, 3), 18)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0, 3), 0)
    def test_perimeter_neg(self):
        x, y, z = -5, -12, -13
        self.assertEqual(perimeter(x, y, z), -30)
