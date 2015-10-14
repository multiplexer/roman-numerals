import unittest

# Requires PEP8 checking for style -- automatically enabled in pycharm.
#
# This little library performs both the transform from roman numerals to decimals and decimals
# to roman numerals.  The simpler transform is simply iterative adds and subtracts.  The more difficult
# can be solved elegantly with a little fancy recursion.

def recurse_d_to_r(val, roman, decimals, romanNumerals):
    # Functional programming version.  We solve for the smallest case and then the common case.
    # If val is less than the current head of the decimals list then we keep recursing the list.
    # If val is equal or greater, we have a hit. We move the value from the roman numerals into our accumulator string and
    # recurse with the same value until the val accumulator drops below the next decimal.
    # This is much simpler do to with if/then/else but much longer. :)
    # Another solution is to do it with mods and individual accumulators.

    if decimals:
        if val < decimals[0]:
            # Recurse the tail
            return recurse_d_to_r(val, roman, decimals[1:], romanNumerals[1:])
        else:
            # Remove the current decimal value from the val, attach the roman letter, recurse the data structure
            return recurse_d_to_r(val - decimals[0], roman + romanNumerals[0], decimals, romanNumerals)
    else:
        return roman


def convert_d_to_r(val):
    # The setup.  This is all the valid 1 and 2 letter combos available.

    decimals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanNumerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    if val < 0:
        raise ValueError

    if val > 3999:
        raise ValueError

    return recurse_d_to_r(val, "", decimals, romanNumerals)


def convert_r_to_d(roman):
    # Algorithm for convert roman to decimal is to read the string, reverse the string, read right from left.
    # If the character is > than maximum, add to accumulator and increase maximum.
    # If the character is < than maximum, decrease accumulator.

    accumulator = 0
    maximum = 0

    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for c in roman[::-1]:
        if max(maximum, lookup[c]):
            accumulator += lookup[c]
            maximum = lookup[c]
        else:
            accumulator -= lookup[c]

    return accumulator


class DecToRomanTest(unittest.TestCase):
    def testSmallestRomanToDecimal(self):
        self.assertEqual('1', convert_r_to_d("I"))

    def testRomanToDecimal(self):
        self.assertEqual('1365', convert_r_to_d("MCCCLXV"))

    def testSmallest(self):
        self.assertEqual('I', convert_d_to_r(1))

    def testVI(self):
        self.assertEqual('VI', convert_d_to_r(6))

    def testIX(self):
        self.assertEqual('IX', convert_d_to_r(9))

    def testXVIII(self):
        self.assertEqual('XVIII', convert_d_to_r(18))

    def testXIX(self):
        self.assertEqual('XIX', convert_d_to_r(19))

    def testXXXVIII(self):
        self.assertEqual('XXXVIII', convert_d_to_r(38))

    def testXXXIX(self):
        self.assertEqual('XXXIX', convert_d_to_r(39))

    def testXL(self):
        self.assertEqual('XL', convert_d_to_r(40))

    def testXCVIII(self):
        self.assertEqual('XCVIII', convert_d_to_r(98))

    def testCCCLXXXVIII(self):
        self.assertEqual('CCCLXXXVIII', convert_d_to_r(388))

    def testCDXCIX(self):
        self.assertEqual('CDXCIX', convert_d_to_r(499))

    def testDCCCLXVII(self):
        self.assertEqual('DCCCLXVII', convert_d_to_r(867))

    def testMCMXCVIII(self):
        self.assertEqual('MCMXCVIII', convert_d_to_r(1998))

    def testMMMCMXCIX(self):
        self.assertEqual('MMMCMXCIX', convert_d_to_r(3999))


if __name__ == "__main__":
    unittest.main()
