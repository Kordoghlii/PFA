import unittest
from filename_utils import *

class TestFilenameUtils(unittest.TestCase):
    def test_get_extension(self):
        self.assertEqual(get_extension("image.png"), "png")
        self.assertEqual(get_extension("noext"), "")

    def test_remove_extension(self):
        self.assertEqual(remove_extension("image.png"), "image")
        self.assertEqual(remove_extension("noext"), "noext")

    def test_is_valid_filename(self):
        self.assertTrue(is_valid_filename("image.png"))
        self.assertFalse(is_valid_filename("image?.png"))

    def test_add_suffix(self):
        self.assertEqual(add_suffix("image.png", "_backup"), "image_backup.png")
        self.assertEqual(add_suffix("noext", "_backup"), "noext_backup")

    def test_replace_extension(self):
        self.assertEqual(replace_extension("image.png", "jpg"), "image.jpg")
        self.assertEqual(replace_extension("noext", "txt"), "noext.txt")

    def test_get_basename(self):
        self.assertEqual(get_basename("/path/to/image.png"), "image.png")
        self.assertEqual(get_basename("image.png"), "image.png")

    def test_get_path(self):
        self.assertEqual(get_path("/path/to/image.png"), "/path/to")
        self.assertEqual(get_path("image.png"), "")

    def test_normalize_filename(self):
        self.assertEqual(normalize_filename("my file.png"), "my_file.png")
        self.assertEqual(normalize_filename("file"), "file")

    def test_is_image_file(self):
        self.assertTrue(is_image_file("image.PNG"))
        self.assertFalse(is_image_file("doc.txt"))

    def test_truncate_filename(self):
        self.assertEqual(truncate_filename("longfilename.png", 10), "longf.png")
        self.assertEqual(truncate_filename("short.txt", 20), "short.txt")

if __name__ == '__main__':
    unittest.main()