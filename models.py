from itertools import product


class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        if self.quantity >= quantity:
            return True
        else:
            return False


    def buy(self, quantity):
        if quantity == 0:
            raise ValueError('Количество продукта должно быть больше 0!')
        elif self.check_quantity(quantity):
            self.quantity -= quantity
            return True
        else:
            raise ValueError('Недостаточное количество данного продукта!')


    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        if product.check_quantity(buy_count) and buy_count > 0:
            if product in self.products:
                self.products[product] += buy_count
            else:
                self.products[product] = buy_count
        elif buy_count == 0:
            raise ValueError('Количество продукта должно быть больше 0!')
        else:
            raise ValueError('Недостаточное количество данного продукта!')


    def remove_product(self, product: Product, remove_count=None):
        if remove_count == 0:
            raise ValueError('Количество продукта должно быть больше 0!')
        elif remove_count is None or remove_count >= self.products[product]:
            self.products.pop(product)
        elif self.products[product] > remove_count > 0:
            if product in self.products:
                self.products[product] -= remove_count
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """


    def clear(self):
        self.products = {}


    def get_total_price(self) -> float:
        total_price = 0
        for product in self.products.keys():
            total_price += product.price * self.products.get(product)
        return total_price


    def buy(self):
        for product in self.products.keys():
            product.buy(self.products.get(product))

        self.clear()
