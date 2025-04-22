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
        if buy_count <= 0:
            raise ValueError('Количество продукта должно быть больше 0!')
        if not product.check_quantity(buy_count):
            raise ValueError('Недостаточное количество данного продукта!')
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count


    def remove_product(self, product: Product, remove_count=None):
        if product not in self.products:
            raise ValueError('Данного продукта нет в корзине!')
        if remove_count is None or self.products[product] <= remove_count:
            self.products.pop(product)
        elif remove_count <= 0:
            raise ValueError('Количество продукта должно быть больше 0!')
        else:
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
        if not self.products:
            raise ValueError('Товары в корзине отсутствуют!')
        for product, quantity in self.products.items():
            if not product.check_quantity(quantity):
                raise ValueError('Недостаточное количество данного продукта!')
            product.buy(self.products.get(product))
        self.clear()

