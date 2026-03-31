import pytest
from unittest.mock import Mock
from praktikum.burger import Burger

class TestBurger:

    def test_set_buns_sets_bun_correctly(self):
        burger = Burger()
        bun = Mock()

        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient_adds_ingredient_to_list(self):
        burger = Burger()
        ingredient = Mock()

        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_removes_ingredient_by_index(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.remove_ingredient(0)

        assert burger.ingredients == [ingredient2]

    def test_move_ingredient_moves_ingredient_to_new_position(self):
        burger = Burger()
        ingredient1 = Mock()
        ingredient2 = Mock()
        ingredient3 = Mock()

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.add_ingredient(ingredient3)
        burger.move_ingredient(0, 2)

        assert burger.ingredients == [ingredient2, ingredient3, ingredient1]

    @pytest.mark.parametrize('bun_price, ingredients_prices, expected', [
        (100, [50, 50], 300),
        (200, [], 400),
        (50, [25], 125),
    ])

    def test_get_price_returns_correct_total_price(self, bun_price, ingredients_prices, expected):
        burger = Burger()
        bun = Mock()

        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredients_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)
        
        assert burger.get_price() == expected

    def test_get_receipt_returns_correct_receipt_string(self):
        burger = Burger()
        bun = Mock()

        bun.get_name.return_value = 'black bun'
        bun.get_price.return_value = 100

        ingredient = Mock()
        ingredient.get_type.return_value = 'SAUCE'
        ingredient.get_name.return_value = 'ketchup'
        ingredient.get_price.return_value = 50

        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        receipt = burger.get_receipt()

        expected = (
            "(==== black bun ====)\n"
            "= sauce ketchup =\n"
            "(==== black bun ====)\n\n"
            "Price: 250"
        )

        assert receipt == expected