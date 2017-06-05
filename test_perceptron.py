from unittest import TestCase
import unittest
import perceptron
class TestPerceptron(unittest.TestCase):
    def setUp(self):
        self._x =  0.1
        self._y = 0.3

    #test*としないとテストが読み込まれない。
    def testAdd(self):
        actual = perceptron.AND(self._x, self._y)
        expected = 0
        self.assertAlmostEquals(actual, expected)

    def tearDown(self):
        print("perceptron")
