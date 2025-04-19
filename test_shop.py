"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture()
def product_book() -> Product:
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture()
def product_mobile_phone() -> Product:
    return Product("mobile_phone", 12000, "This is a phone", 50)

@pytest.fixture()
def cart() -> Cart:
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product_book):
        assert product_book.check_quantity(product_book.quantity)


    def test_product_check_quantity_available(self, product_book):
        assert not product_book.check_quantity(product_book.quantity + 1)


    def test_product_buy(self, product_book):
        quantity_available = product_book.quantity
        quantity_to_purchase = product_book.quantity//10
        product_book.buy(quantity_to_purchase)
        assert product_book.quantity == quantity_available - quantity_to_purchase


    def test_product_buy_more_than_available(self, product_book):
        with pytest.raises(ValueError):
            product_book.buy(product_book.quantity + 1)


class TestCart:

    def test_add_product(self, product_book, cart):
        cart.add_product(product_book, 50)
        assert cart.products[product_book] == 50

    def test_add_quantity(self, product_book, cart):
        cart.add_product(product_book, 100)
        cart.add_product(product_book, 50)
        assert cart.products[product_book] == 150

    def test_add_two_products(self, product_book, product_mobile_phone, cart):
        cart.add_product(product_book, 60)
        cart.add_product(product_mobile_phone, 10)
        assert cart.products[product_book] == 60
        assert cart.products[product_mobile_phone] == 10

    def test_add_product_more_than_available(self, product_book, cart):
        with pytest.raises(ValueError):
            cart.add_product(product_book, (product_book.quantity + 10))

    def test_add_zero_quantity(self, product_mobile_phone, cart):
        with pytest.raises(ValueError):
            cart.add_product(product_mobile_phone, 0)


    def test_remove_product(self, product_book, cart):
        quantity_to_purchase = 100
        quantity_to_be_removed = 50
        cart.add_product(product_book, quantity_to_purchase)
        cart.remove_product(product_book, quantity_to_be_removed)
        assert cart.products[product_book] == quantity_to_purchase - quantity_to_be_removed

    def test_remove_product_more_than_available(self, product_book, cart):
        quantity_to_purchase = 100
        quantity_to_be_removed = 115
        cart.add_product(product_book, quantity_to_purchase)
        cart.remove_product(product_book, quantity_to_be_removed)
        assert len(cart.products) == 0

    def test_remove_product_with_none(self, product_book, cart):
        cart.add_product(product_book, 150)
        cart.remove_product(product_book)
        assert len(cart.products) == 0

    def test_removing_one_of_the_products(self, product_book, product_mobile_phone, cart):
        cart.add_product(product_book, 200)
        cart.add_product(product_mobile_phone, 15)
        cart.remove_product(product_book, 100)
        assert cart.products[product_book] == 100
        assert cart.products[product_mobile_phone] == 15


        var = ("\n"
               "    TODO Напишите тесты на методы класса Cart\n"
               "        На каждый метод у вас должен получиться отдельный тест\n"
               "        На некоторые методы у вас может быть несколько тестов.\n"
               "        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)\n"
               "    ")
