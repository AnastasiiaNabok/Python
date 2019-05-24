import math


class Triangle:
    def __init__(self, name, side1, side2, side3):
        self.name = name
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.area = self.__calculate_area()

    def __calculate_area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return round(area, 2)


def split_inputs(triangle):
    triangle_parsed = {}
    triangle = triangle.replace(' ', '').split(',')
    name = triangle[0]
    sides = []
    for side in triangle[1:]:
        sides.append(side)
    triangle_parsed.update({'name': name, 'sides': sides})
    return triangle_parsed


def validate_inputs(triangle_parsed):
    if len(triangle_parsed['sides']) != 3:
        raise ValueError('Please provide us 3 sides')

    for side in triangle_parsed['sides']:
        if not side.isdigit():
            raise ValueError(f'"{side}" is not a number')

    side1 = float(triangle_parsed['sides'][0])
    side2 = float(triangle_parsed['sides'][1])
    side3 = float(triangle_parsed['sides'][2])

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        return triangle_parsed['name'], side1, side2, side3
    else:
        raise ValueError('Triangle with given sides does not exist')


def main():
    triangles_list = []
    while True:
        triangle = split_inputs(input('Please enter triangle name, side1, side2, side3 comma separated: '))
        try:
            name, side1, side2, side3 = validate_inputs(triangle)
            triangles_list.append(Triangle(name, side1, side2, side3))
        except ValueError as e:
            print(e)
        else:
            add_new = input('Press "y" or "yes" if you want to continue.  Press any key if you want to stop. ')
            if add_new.lower() == 'y' or add_new.lower == "yes":
                continue
            else:
                break
    return triangles_list


if __name__ == '__main__':
    triangles = main()
    triangles.sort(key=lambda x: x.area, reverse=True)
    print('============= Triangles list: ===============')
    for t in triangles:
        print(f'"{t.name}": {t.area} cm')

