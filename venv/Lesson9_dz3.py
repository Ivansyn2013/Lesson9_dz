class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def full_name(self):
        return f'{self.name} {self.surname} '

    def get_profit(self):
        return f'{sum(self._income.values())}'


some_body = Position('Ivanov', 'Ivan', 'catcher', 10000, 7500)

print(some_body.full_name())
print(some_body.position)
print(some_body.get_profit())
