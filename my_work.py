class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        #pass

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity
        #pass

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * self.quantity * self.all
        #pass

item = Item('apple', 20.0, 3)

assert item.calculate_total_price() == 60.0
assert item.apply_discount() == 51.0