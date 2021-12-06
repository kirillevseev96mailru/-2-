class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Класс нанесения - Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Класс нанесения - Карандаш')


class Handle(Stationery):
    def draw(self):
        print('Класс нанесения - Маркер')


pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

pen.draw()
pencil.draw()
handle.draw()