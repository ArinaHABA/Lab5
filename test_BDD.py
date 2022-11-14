
from behave import *  # импорт из behave
from test_TDD import *  # импорт из test_TDD


@given('Burger_Builder')
def first_step(context):
    context.a = Burger_Test_Builder()


@when('test_hamburger_builder return OK')
def test_hamburger_builder(context):
    context.a.test_hamburger_builder()


@when('test_cheeseburger_builder return OK')
def test_cheeseburger_builder(context):
    context.a.test_cheeseburger_builder()


@then('Successfully')
def last_step(context):
    pass