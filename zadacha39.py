class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._in_wage = income['wage']
        self._in_bonus = income['bonus']

class Position(Worker):

    def get_total_income(self):
        return self._in_wage + self._in_bonus

    def get_full_name(self):
        return f'{self.name} {self.surname} {self.position}'



pos = Position('Kirill', 'Evseev', 'logger', {"wage": 100000, "bonus": 50000})
print(pos.get_full_name())
print(pos.get_total_income())