class Resistor:
    """
    A class representing a resistor with a color code that specifies its resistance and tolerance.

    Attributes:
    - color_code (list of str): A list of three or four strings representing the colors of the resistor's bands.

    Methods:
        - resistance(): Returns the resistance value of the resistor in ohms, calculated from its color code.
        - tolerance(): Returns the tolerance of the resistor in percentage, based on its color code.
        - __str__(): Returns a string representation of the resistor in the format "Resistor with color code
         {color_code} has a resistance of {resistance} ohms and tolerance of {tolerance}%".

        Color codes:
        - The first two colors represent the significant digits of the resistance value.
        - The third color represents the multiplier, which is a power of ten.
        - The optional fourth color represents the tolerance, which is either 5% for gold or 10% for silver, or 20% if
        absent.

        Resistance calculation:
        - The resistance value is calculated as (digit1 * 10 + digit2) * 10^multiplier, where digit1 and digit2 are the
         values corresponding to the first and second colors, and multiplier is the value corresponding to the third
         color.
        """

    def __init__(self, color_code):
        self.color_code = color_code

    def resistance(self):
        color_codes = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
                       "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9}
        resistance_value = (color_codes[self.color_code[0]] * 10 + color_codes[self.color_code[1]]) * \
                           (10 ** color_codes[self.color_code[2]])
        return resistance_value

    def tolerance(self):
        tolerance_codes = {"gold": 5, "silver": 10}
        if len(self.color_code) == 4:
            return tolerance_codes[self.color_code[3]]
        else:
            return 20

    def __str__(self):
        return f"Resistor with color code {self.color_code} has a resistance of {self.resistance()}" \
               f" ohms and tolerance of {self.tolerance()}%"


if __name__ == '__main__':
    resistor = Resistor(["brown", "black", "red", "gold"])

    print(resistor.tolerance())
# Output: 5

    print(resistor.resistance())
# Output: 1200
