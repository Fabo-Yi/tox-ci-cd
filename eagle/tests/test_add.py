from eagle import adder
import math


class TestClass(object):
    def test_adder(self):
        assert adder.add(3, 5) == 8

    def test_two(self):
        sample = "hello"
        assert hasattr(sample, 'split')

    def test_sqr(self):
        assert math.sqrt(9) == 3
