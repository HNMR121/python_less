class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск оторисовки {self.title}")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)


b = Pen("Ручка")
c = Pencil('Карандаш')
d = Handle("маркер")

b.draw()
c.draw()
d.draw()


