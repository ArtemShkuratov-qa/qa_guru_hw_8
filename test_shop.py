"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def product_book() -> Product:
    book = Product("book", 100, "This is a book", 1000)
    return book

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





        var = ("\n"
               "    TODO Напишите тесты на методы класса Cart\n"
               "        На каждый метод у вас должен получиться отдельный тест\n"
               "        На некоторые методы у вас может быть несколько тестов.\n"
               "        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)\n"
               "    ")
