class Pyramid:
    def __init__(self, height):
        self.height = height

    def print_star_pyramid(self):
        for i in range(self.height, 0, -1):
            print(" " * (self.height - i) + "*" * (2 * i - 1))


height = int(input("피라미드 높이를 입력하세요: "))
p = Pyramid(height)
p.print_star_pyramid()

#commit 