import unittest
import passtool


class TestPasstool(unittest.TestCase):
    def test_common_is_weak(self):
        self.assertEqual(passtool.rate("password"), "weak")

    def test_long_random_is_strong(self):
        self.assertEqual(passtool.rate("k9#Vq2!xLm8@Zp4wRt"), "strong")

    def test_generate_length(self):
        self.assertEqual(len(passtool.generate(24)), 24)


if __name__ == "__main__":
    unittest.main()
