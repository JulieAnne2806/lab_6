class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError(f"Invalid triangle sides: {a}, {b}, {c}")
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        if a == b:
            raise ValueError(f"Invalid trapeze: bases cannot be equal (a={a}, b={b})")
        self.a, self.b, self.c, self.d = a, b, c, d

    def area(self):
        s = (self.a + self.b + self.c + self.d) / 2
        under_root = (s - self.a) * (s - self.b) * (s - self.a - self.c) * (s - self.a - self.d)

        if under_root < 0:
            print(f"Warning: Complex area detected in Trapeze with sides {self.a}, {self.b}, {self.c}, {self.d}")
            return 0
        h = (under_root ** 0.5) / abs(self.a - self.b)
        return ((self.a + self.b) / 2) * h

    def perimeter(self):
        return self.a + self.b + self.c + self.d


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def area(self):
        return self.a * self.h

    def perimeter(self):
        return 2 * (self.a + self.b)


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.141592653589793 * self.r ** 2

    def perimeter(self):
        return 2 * 3.141592653589793 * self.r


def read_figures(filename):
    figures = []
    with open(filename, "r") as file:
        for line in file:
            data = line.split()
            if not data:
                continue
            shape = data[0]
            try:
                params = list(map(float, data[1:]))
                if shape == "Triangle":
                    figures.append(Triangle(*params))
                elif shape == "Rectangle":
                    figures.append(Rectangle(*params))
                elif shape == "Trapeze":
                    figures.append(Trapeze(*params))
                elif shape == "Parallelogram":
                    figures.append(Parallelogram(*params))
                elif shape == "Circle":
                    figures.append(Circle(*params))
            except ValueError as e:
                print(f"Error processing line '{line.strip()}': {e}")
    return figures


def find_largest(figures):
    max_area_figure = max(figures, key=lambda f: f.area())
    max_perimeter_figure = max(figures, key=lambda f: f.perimeter())
    return max_area_figure, max_perimeter_figure


def main():
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    all_figures = []

    for file in input_files:
        all_figures.extend(read_figures(file))

    for figure in all_figures:
        print(f"Type: {type(figure).__name__}, Area: {figure.area()}, Perimeter: {figure.perimeter()}")

    max_area_figure, max_perimeter_figure = find_largest(all_figures)

    with open("output.txt", "w") as output:
        output.write(f"Figure with max area: {type(max_area_figure).__name__} - {max_area_figure.area()}\n")
        output.write(f"Figure with max perimeter: {type(max_perimeter_figure).__name__} - {max_perimeter_figure.perimeter()}\n")

    print("Results saved to output.txt")


if __name__ == "__main__":
    main()

