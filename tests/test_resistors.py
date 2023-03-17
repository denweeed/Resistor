from src.resistors import Resistor


def test_resistance():
    resistor = Resistor(["brown", "black", "red", "gold"])
    assert resistor.resistance() == 1200

    resistor = Resistor(["yellow", "violet", "brown", "silver"])
    assert resistor.resistance() == 470

    resistor = Resistor(["orange", "orange", "orange"])
    assert resistor.resistance() == 33000


def test_tolerance():
    resistor = Resistor(["brown", "black", "red", "gold"])
    assert resistor.tolerance() == 5

    resistor = Resistor(["yellow", "violet", "brown", "silver"])
    assert resistor.tolerance() == 10

    resistor = Resistor(["orange", "orange", "orange"])
    assert resistor.tolerance() == 20


def test_str():
    resistor = Resistor(["brown", "black", "red", "gold"])
    assert str(
        resistor) == "Resistor with color code ['brown', 'black', 'red', 'gold'] has a resistance of 1200 ohms" \
                     " and tolerance of 5%"

    resistor = Resistor(["yellow", "violet", "brown", "silver"])
    assert str(
        resistor) == "Resistor with color code ['yellow', 'violet', 'brown', 'silver'] has a resistance of 470 ohms" \
                     " and tolerance of 10%"

    resistor = Resistor(["orange", "orange", "orange"])
    assert str(
        resistor) == "Resistor with color code ['orange', 'orange', 'orange'] has a resistance of 33000 ohms" \
                     " and tolerance of 20%"
