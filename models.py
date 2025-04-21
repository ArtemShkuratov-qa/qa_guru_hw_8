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
        return self.quantity >= quantity


    def buy(self, quantity):
        if quantity == 0:
            raise ValueError('Количество продукта должно быть больше 0!')
        elif self.check_quantity(quantity):
            self.quantity -= quantity
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
        if buy_count > 0:
            if product.check_quantity(buy_count):
                if product in self.products:
                    self.products[product] += buy_count
                else:
                    self.products[product] = buy_count
            elif not product.check_quantity(buy_count):
                raise ValueError('Недостаточное количество данного продукта!')
        elif buy_count <= 0:
            raise ValueError('Количество продукта должно быть больше 0!')


    def remove_product(self, product: Product, remove_count=None):
        if remove_count is None or remove_count > 0:
            if product in self.products:
                if remove_count is None or self.products[product] <= remove_count:
                    self.products.pop(product)
                elif self.products[product] > remove_count:
                    self.products[product] -= remove_count
            elif product not in self.products:
                raise ValueError('Данного продукта нет в корзине!')
        elif remove_count <= 0:
            raise ValueError('Количество продукта должно быть больше 0!')

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
        if self.products:
            for product in self.products.keys():
                if product.check_quantity(self.products.get(product)):
                    product.buy(self.products.get(product))
                elif not product.check_quantity(self.products.get(product)):
                    raise ValueError('Недостаточное количество данного продукта!')
            self.clear()
        elif not self.products:
            raise ValueError('Товары в корзине отсутствуют!')

