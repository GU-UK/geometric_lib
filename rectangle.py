def area(a, b):
    '''
    Вовращает площадь прямоугольника.

        Параметры:
            a (int): десятичное целое число.
            b (int): десятичное целое число.

        Возвращаемое значение:
            a * b (int): десятичное целое число.
        Пример:
        area(4, 5)  =>  4 * 5 = 20
    '''
    return a * b


def perimeter(a, b):
    '''
    Вовращает периметр прямоугольника.
    
        Параметры:
            a (int): десятичное целое число.
            b (int): десятичное целое число.

        Возвращаемое значение:
            a * 2 + b * 2 (int): десятичное целое число.
        Пример:
        perimeter(4, 5)  =>  4*2 + 5*2 = 26
    '''
    return a*2 + b*2


import unittest
class RectangleTestCase(unittest.TestCase):
    def test_area_rectangle(self):
        self.assertEqual(area(10, 5), 50)
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
    def test_area_nointegers(self):
        res = area(9.3, 4.1)
        self.assertEqual(res, 38.13)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter(10, 5), 30)
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 0)
    def test_perimeter_nointegers(self):
        res = perimeter(9.3, 4.1)
        self.assertEqual(res, 26.8)