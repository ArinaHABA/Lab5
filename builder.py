from __future__ import annotations  # для аннотаций ->
from abc import ABC, abstractmethod  # для использования абстракции
from typing import Any  # Средство проверки статического типа
# для значения типа Any и присвоить его любой переменной

# Строитель — это порождающий паттерн проектирования, который позволяет создавать сложные объекты пошагово.
# Строитель даёт возможность использовать один и тот же код строительства для получения разных представлений объектов.
class Builder(ABC):
    @property  # property позволяет превратить метод класса в атрибут класса

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:  # проверка типов аргументов и возвращаемое значение функции
        pass

    @abstractmethod
    def buns(self) -> None:  # булочки
        pass

    @abstractmethod
    def cutlet(self) -> None:  # котлета
        pass

    @abstractmethod
    def pickles(self) -> None:  # огурчики
        pass

    @abstractmethod
    def cheese(self) -> None:  # сыр
        pass

    @abstractmethod
    def ketchup(self) -> None:  # кетчуп
        pass

class Burger_Builder(Builder):  # строитель бургера
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:  # функция сброса
        self._product = Burger()

    @property  # property позволяет превратить метод класса в атрибут класса
    def product(self) -> Burger:
        product = self._product
        self.reset()
        return product

    def buns(self) -> None:
        self._product.add("булочки")

    def cutlet(self) -> None:
        self._product.add("котлета")

    def pickles(self) -> None:
        self._product.add("огурчики")

    def cheese(self) -> None:
        self._product.add("сыр")

    def ketchup(self) -> None:
        self._product.add("кетчуп")

class Burger:
    def __init__(self) -> None:
        self.parts = []  # parts - части

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В состав входят: {', '.join(self.parts)}", end="")

class Director:  # директор отвечает только за выполнение шагов построения в определённой последовательности
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  # применяется сеттер к методу builder, то есть делаем метод доступным для записи
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def Hamburger(self) -> None:
        self.builder.buns()
        self.builder.cutlet()
        self.builder.pickles()
        self.builder.ketchup()

    def Cheeseburger(self) -> None:
        self.builder.buns()
        self.builder.cutlet()
        self.builder.cheese()
        self.builder.ketchup()

if __name__ == "__main__":
    director = Director()  # наследование класса
    builder = Burger_Builder()
    director.builder = builder
    print("Гамбургер:")
    director.Hamburger()
    builder.product.list_parts()
    print('\n')
    print("Чизбургер:")
    director.Cheeseburger()
    builder.product.list_parts()