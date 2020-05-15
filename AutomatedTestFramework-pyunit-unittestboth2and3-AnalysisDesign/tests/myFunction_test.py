import unittest
import sys
sys.path.append("/Users/family/Downloads/AutomatedTestFramework-python-pyunit-aka-unittest-AnalysisDesign/src/")
from myFunction import Sum 

class SumTest(unittest.TestCase):
    def test_Sum(self):
        self.assertEqual(Sum(1, 1), 2)
	#self.assertEqual(Sum(1,1),100)
        self.assertTrue(Sum(10, 20) == 30)
	#self.assertTrue(Sum(10,20) == 1000)
