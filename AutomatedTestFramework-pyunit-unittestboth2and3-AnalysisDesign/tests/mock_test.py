import unittest
import mock
import sys
sys.path.append("/Users/family/Downloads/AutomatedTestFramework-python-pyunit-aka-unittest-AnalysisDesign/src")
from myFunction import Random

class RandomTest(unittest.TestCase):
    @mock.patch('os.urandom')
    def test_Random(self, random_mock):
        random_mock.return_value = 'aaa'
        self.assertEqual(Random(2), '2aaa')
	#self.assertEqual(Random(2), '3aaa')
