import unittest
from SRC import List

class TestMyList(unittest.TestCase):
    def setUp(self):
        self.ml = List.my_list(12, 341, 32, 4, 234, "hello", "world")
    def test_repr(self):
        self.assertEqual(str(self.ml), str([12, 341, 32, 4, 234, "hello", "world"]))
    def test_len(self):
        self.assertEqual(len(self.ml), 7)
    def test_getitem(self):
        self.assertEqual(self.ml[1], 341)
    def test_setitem(self):
        self.ml[1] = "Hi"
        self.assertEqual(self.ml[1], "Hi")
    def test_reverse(self):
        self.assertEqual(str(self.ml.__reversed__()), str([12, 341, 32, 4, 234, "hello", "world"].reverse()))
    def test_pop(self):
        self.assertEqual(self.ml.pop(), "world")
    def test_append(self):
        self.ml.append("good")
        self.assertEqual("good", self.ml[-1])