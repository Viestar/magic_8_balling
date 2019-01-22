
import unittest
from game import magic8Ball

class TestMagicBallers(unittest.TestCase):

    def test_magic8Ball(self):
        self.assertEqual(magic8Ball("can i Andela?"), "Yes")
        


if __name__ == '__main__':
    unittest.main()