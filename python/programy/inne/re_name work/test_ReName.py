import unittest
from ReName_filer_v1_6 import Tree, StartAction, ReName
from nested import nested
import os


class TestTree(unittest.TestCase):
    
    def test_getDrivesName(self):
        gdN = Tree()
        self.assertNotEqual([], gdN.getDrivesName())
'''
class TestStartAction(unittest.TestCase):
    
    def test_actionLoop(self):
        sAction = StartAction()
        location = '/home/micha/Pulpit/zmiana'
        full_oldName = os.path.join(location, 'EQUIP_MOV_13112022w31MiG.EQP')
        nestedRenameFunc = nested(sAction.actionLoop, 'renameFunc', preview = 'No')
        self.assertNotEqual('EQUIP_BIO_13112022w31MiG.EQP', nestedRenameFunc('EQUIP_MOV_13112022w31MiG.EQP', 'EQUIP_BIO_13112022w31MiG.EQP', full_oldName))
'''
class TestReName(unittest.TestCase): 

    def test_textFieldAutoFit1(self):
        obj = ReName()
        self.assertAlmostEqual(obj.textFieldAutoFit('Bioly_1'), 6.5325) 
        self.assertEqual(obj.textFieldAutoFit('aaa'), 3.12)
                     

if __name__ == '__main__':
    unittest.main(verbosity=2)