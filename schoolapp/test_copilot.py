# write a function to reverse a string
# ...existing code...
def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]


# simple unit tests
import unittest

class TestReverseString(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("🙂👍"), "👍🙂")

if __name__ == "__main__":
    unittest.main()
# ...existing code...