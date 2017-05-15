'''
Created on Oct 27, 2015

@author: Avery
'''
import unittest
import DVRouter
import RoutingTable


class Test(unittest.TestCase):


    def testAddLink(self):
        r1 = DVRouter.DVRouter('B')
        r1.addLink('C', 1.2)
        r1.addLink('A', 2.3)
        self.assertTrue('C' in r1.links)
        self.assertTrue(r1.rTable.contains('C'))
        self.assertTrue('A' in r1.links)
        self.assertTrue(r1.rTable.contains('A'))
        #Make a duplicate routing table
    
    def testRemoveLink(self):
        r1 = DVRouter.DVRouter('B')
        r1.addLink('C', 1.2)
        r1.addLink('A', 2.3)
        self.assertTrue('C' in r1.links)
        self.assertTrue(r1.rTable.contains('C'))
        self.assertTrue('A' in r1.links)
        self.assertTrue(r1.rTable.contains('A'))
        r1.removeLink('C')
        self.assertFalse('C' in r1.links)
        self.assertFalse(r1.rTable.contains('C'))
        r1.removeLink('A')
        self.assertFalse('A' in r1.links)
        self.assertFalse(r1.rTable.contains('A'))
    
    def testExport(self):
        r1 = DVRouter.DVRouter('B')
        r1.addLink('C', 1.2)
        r1.addLink('A', 2.3)
        r2 = DVRouter.DVRouter('C')
        r2.addLink('B', 1.6)
        r2.addLink('A', 2.5)
        r3 = DVRouter.DVRouter('D')
        r3.addLink('C', 1.6)
        #Create a duplicate routing table
        table = r1.export()
        self.assertEqual(table, r1.rTable)
        table1 = r2.export()
        self.assertEqual(table1, r2.rTable)
        table2 = r3.export()
        self.assertEqual(table2, r3.rTable)

    def testImport(self):
        r1 = DVRouter.DVRouter('A')
        r1.addLink('B', 1.5)
        r1.addLink('C', 1.2)
        r2 = DVRouter.DVRouter('B')
        r2.addLink('C', 1.0)
        r2.addLink('A', 1.5)
        r2.addLink('D', 1.3)
        r3 = DVRouter.DVRouter('C')
        r3.addLink('A', 1.2)
        r3.addLink('B', 1.0)
        r4 = DVRouter.DVRouter('D')
        r4.addLink('B', 1.3)
        r1.rimport([r2.export(), r3.export()])
        self.assertTrue(r1.rTable.contains('D'))
        self.assertTrue(r1.rTable.getVector('D').dist == 2.8)
        self.assertTrue(r1.rTable.getVector('D').first_hop == 'B')
        self.assertTrue(r1.rTable.getVector('B').dist == 1.5)
        self.assertTrue(r1.rTable.getVector('C').dist == 1.2)
        self.assertTrue(r1.rTable.getVector('A').dist == 0)
        r2.rimport([r1.export(), r3.export()])
        self.assertTrue(r2.rTable.getVector('D').dist == 1.3)
        self.assertTrue(r2.rTable.getVector('A').dist == 1.5)
        self.assertTrue(r2.rTable.getVector('B').dist == 0)
        self.assertTrue(r2.rTable.getVector('C').dist == 1.0)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()