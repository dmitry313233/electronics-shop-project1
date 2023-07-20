from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return int(f'{self.__number_of_sim}')

    @number_of_sim.setter
    def number_of_sim(self, num):
        if num > 0 and isinstance(num, int):
            self.__number_of_sim = num
        else:
            self.__number_of_sim = 1
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')