from src.item import Item



class MixinLog:
    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
            return self
        else:
            self.language = 'EN'
            return self

    @property
    def languages(self):
        return self.__language



class Keyboard(Item, MixinLog):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = 'EN'

