# Stellar Burgers — QA Python Project

Учебный проект по тестированию Python-классов для системы заказа бургеров **Stellar Burgers**.

В этом проекте реализована модель бургера с булками и ингредиентами, а также написаны юнит-тесты для класса `Burger`.

## Структура проекта

Diplom_1/
├── praktikum/
│ ├── init.py
│ ├── burger.py 
│ ├── bun.py 
│ ├── ingredient.py 
│ ├── ingredient_types.py
│ ├── database.py
│ └── praktikum.py 
└── tests/
└── test_burger.py


## Классы

### Burger

- `set_buns(bun)` — устанавливает булку
- `add_ingredient(ingredient)` — добавляет ингредиент
- `remove_ingredient(index)` — удаляет ингредиент по индексу
- `move_ingredient(index, new_index)` — перемещает ингредиент
- `get_price()` — возвращает общую стоимость бургера
- `get_receipt()` — возвращает строку с чеком бургера

## Тесты

- Все тесты находятся в `tests/test_burger.py`
- Используются:
  - **pytest** для запуска
  - **pytest-cov** для проверки покрытия
  - **unittest.mock.Mock** для изоляции зависимостей
  - **параметризация** для проверки разных кейсов цены
- Покрыты **все методы класса `Burger`** → покрытие **100%**

## Установка и запуск

1. Установить зависимости:

```bash
pip install pytest pytest-cov
Запуск тестов с покрытием:
cd /path/to/Diplom_1
PYTHONPATH=. pytest --cov=praktikum
Ожидаемый результат:
tests/test_burger.py ........ [100%]
TOTAL coverage for praktikum/burger.py: 100%
