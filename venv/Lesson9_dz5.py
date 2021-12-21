class Stationery:
    def __init__(self, title='Something that can drow'):
        self.title = title

    def draw(self):
        print(f'Start to  draw {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Pen drowing {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Pencil drowing {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Handle drowing {self.title}')


start = Stationery()
start.draw()
pen = Pen('Parker')
pen.draw()
pencil = Pencil('carc')
pencil.draw()
marker = Handle('jijii')
marker.draw()
