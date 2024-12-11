
def area(a):
    '''
    Вовращает площадь квадрата.

        Параметры:
            a (int): десятичное целое число.

        Возвращаемое значение:
            a * a (int): десятичное целое число.
        Пример:
        area(3)  =>  3 * 3 = 9
    '''
    return a * a


def perimeter(a):
    '''
    Вовращает периметр квадрата.

        Параметры:
            a (int): десятичное целое число.

        Возвращаемое значение:
            4 * a (int): десятичное целое число.
        Пример:
        perimeter(3)  =>  4 * 3 = 12
    '''
    return 4 * a


import unittest
class SquareTestCase(unittest.TestCase):
    def test_area_square(self):
        self.assertEqual(area(10), 100)
    def test_area_zero(self):
        self.assertEqual(area(0), 0)
    def test_area_nointeger(self):
        res = area(9.3)
        self.assertAlmostEqual(res, 86.4900, places=4)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10), 40)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_nointeger(self):
        res = perimeter(9.3)
        self.assertEqual(res, 37.2)
