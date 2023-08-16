import unittest
from .utils import translator_word


class TestTranslateWord(unittest.TestCase):

    def test_convert_video_title(self):
        result_func = translator_word('мир', lang='en')
        self.assertEqual(result_func, 'world')


if __name__ == '__name__':
    unittest.main()
