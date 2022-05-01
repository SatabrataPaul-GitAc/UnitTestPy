import unittest
from volume_cuboid import volume_cuboid

class TestVolume(unittest.TestCase):
    def test_volume(self):
        result = volume_cuboid(5, 6, 3)
        self.assertEqual(result, 90)

if __name__ == "__main__":
    unittest.main()



