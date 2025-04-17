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
        if self.check_quantity(quantity):
            self.quantity -= quantity
            return True
        else:
            raise ValueError


    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
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
        else:
            raise ValueError('Недостаточное количество данного продукта')


    def remove_product(self, product: Product, remove_count=None):
        if self.products[product] > remove_count > 0:
            if product in self.products:
                self.products[product] -= remove_count
        elif remove_count > self.products[product] or remove_count is None:
            self.products.pop(product)

        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """

    def clear(self):
        raise NotImplementedError

    def get_total_price(self) -> float:
        raise NotImplementedError

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        raise NotImplementedError
