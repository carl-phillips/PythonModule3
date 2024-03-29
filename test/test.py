import unittest
from unittest import mock
from fomat_output import average_scores

class test(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85,90,95]):
            assert average_scores.average(85, 90, 95) == 90

if __name__ == '__main__':
    unittest.main()
