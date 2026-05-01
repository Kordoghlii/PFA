import unittest
from string_transforms import *

class TestStringTransforms(unittest.TestCase):
    def test_camel_to_snake(self):
        self.assertEqual(camel_to_snake("helloWorld"), "hello_world")
        self.assertEqual(camel_to_snake("myVarName"), "my_var_name")

    def test_snake_to_camel(self):
        self.assertEqual(snake_to_camel("hello_world"), "helloWorld")
        self.assertEqual(snake_to_camel("my_var_name"), "myVarName")

    def test_remove_extra_spaces(self):
        self.assertEqual(remove_extra_spaces("  hello   world  "), "hello world")
        self.assertEqual(remove_extra_spaces(""), "")

    def test_alternate_case(self):
        self.assertEqual(alternate_case("hello"), "HeLlO")
        self.assertEqual(alternate_case(""), "")

    def test_swap_case(self):
        self.assertEqual(swap_case("Hello"), "hELLO")
        self.assertEqual(swap_case(""), "")

    def test_pad_left(self):
        self.assertEqual(pad_left("hello", 8, "*"), "***hello")
        self.assertEqual(pad_left("", 3, "-"), "---")

    def test_pad_right(self):
        self.assertEqual(pad_right("hello", 8, "*"), "hello***")
        self.assertEqual(pad_right("", 3, "-"), "---")

    def test_truncate_text(self):
        self.assertEqual(truncate_text("hello world", 5), "hello")
        self.assertEqual(truncate_text("hi", 5), "hi")

    def test_repeat_text(self):
        self.assertEqual(repeat_text("hi", 3), "hihihi")
        self.assertEqual(repeat_text("", 5), "")

    def test_wrap_text(self):
        self.assertEqual(wrap_text("hello", "<", ">"), "<hello>")
        self.assertEqual(wrap_text("", "[", "]"), "[]")

if __name__ == '__main__':
    unittest.main()