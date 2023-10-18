import unittest
from ReName_filer_v1_6 import Tree, StartAction, ReName


class TestTree(unittest.TestCase):
    
    def test_getDrivesName(self):
        gdN = Tree()
        self.assertNotEqual([], gdN.getDrivesName())
        



if __name__ == '__main__':
    unittest.main(verbosity=2)