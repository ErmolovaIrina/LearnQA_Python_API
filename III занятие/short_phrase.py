import pytest

class TestShortInput:
    def test_short_input(self):
        phrase = input("Set a phrase: ")
        phraselenth = len(phrase)

        assert phraselenth <= 15, "Wrong lenth, this phrase so long!"