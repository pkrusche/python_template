
import unittest

from module import TestClass


class TestTestClass(unittest.TestCase):
    """ Test class tester
    """

    def test_answer(self):
        t = TestClass()
        sa, a = t.answer_me("Why?")
        self.failUnless(a == 42)
