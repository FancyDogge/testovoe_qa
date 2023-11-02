# проверок на правильность аттрибутов я не делал, т.к. зашиваюсь и это вне скоупа тестового)
import pytest

from task_2.draw_engine import Circle, Triangle, Rectangle, Engine2D


@pytest.fixture
def engine():
    engi = Engine2D()
    return engi


@pytest.fixture
def shapes():
    circle = Circle((0, 1), 5)
    triangle = Triangle([(0, 0), (1, 1), (2, 0)])
    rectangle = Rectangle((1, 1), 3, 2)
    return [circle, triangle, rectangle]


def test_add_shapes_to_canvas(engine, shapes):
    for shape in shapes:
        engine.add_shape(shape)

    assert engine.canvas == shapes


def test_canvas_clearing(engine, shapes):
    for shape in shapes:
        engine.add_shape(shape)

    engine.draw()

    assert engine.canvas == []


def test_color_change(engine, shapes):
    circle = shapes[0]
    engine.set_color("Red")
    engine.add_shape(circle)

    assert circle.color == "Red"


def test_color_change_between_add_shape(engine, shapes):
    circle = shapes[0]
    triangle = shapes[1]

    engine.add_shape(circle)
    engine.set_color("Red")
    engine.add_shape(triangle)

    assert circle.color == "White"
    assert triangle.color == "Red"


def test_draw_method_print(capsys, engine, shapes):
    circle = shapes[0]
    engine.add_shape(circle)
    engine.draw()

    # достаем принт
    captured_output = capsys.readouterr()
    printed_output = captured_output.out.strip().split('\n')[-1]

    expected_output = f"Drawing Circle: {circle.center} with radius {circle.radius}, Color: {circle.color}"

    assert printed_output == expected_output
