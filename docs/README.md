# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Documentation

Эта библиотека предоставляет функции для вычисления площади и периметра различных геометрических фигур. Для каждой фигуры есть файл с функциями

## Треугольник

### Area

`area(a, h)`

Возвращает площадь треугольника с основанием `a` и высотой `h`

Пример работы:
```python
area(4, 2)
4
```

### Perimiter

`perimiter(a, b, c)`

Возвращает периметр треугольника со сторонами `a`, `b` и `c`

Пример работы:
```python
perimiter(1, 2, 3)
6
```

## Прямоугольник

### Area

`area(a, b)`

Возвращает площадь прямоугольника со сторонами `a` и `b`

Пример работы:
```python
area(4, 5)
20
```

### Perimiter

`perimiter(a, b)`

Возвращает периметр прямоугольника со сторонами `a` и `b`

Пример работы:
```python
perimiter(4, 5)
20
```

## Круг

### Area

`area(r)`

Возвращает площадь круга c радиусом `r`

Пример работы:
```python
area(2)
12.566370614359172
```

### Perimiter

`perimiter(r)`

Возвращает периметр (длина окружности) круга с радиусом `r`


Пример работы:
```python
perimiter(3)
18.84955592153876
```

## Квадрат

### Area

`area(a)`

Возвращает площадь квадрата со стороной `a`

Пример работы:
```python
area(3)
9
```

### Perimiter

`perimiter(a)`

Возвращает периметр квадрата со стороной `a`

Пример работы:
```python
perimiter(2)
8
```

# Changelog

- [`b018f9abf62806ec30335ee9b9ab4d0c761c798e`](https://github.com/smartiqaorg/geometric_lib/commit/b018f9abf62806ec30335ee9b9ab4d0c761c798e "Ссылка на коммит") Добавление нового файла "rectangle.py"

- [`f45efa699feef4a7d7f3b33ebf44b168b8fc6d42`](https://github.com/smartiqaorg/geometric_lib/commit/f45efa699feef4a7d7f3b33ebf44b168b8fc6d42 "Ссылка на коммит") Добавление файла "triangle.py" и исправление ошибки в файле "rectangle.py"

