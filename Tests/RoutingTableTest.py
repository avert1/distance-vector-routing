'''
Created on Oct 27, 2015

@author: Avery
'''
import unittest
import RoutingTable


class Test(unittest.TestCase):


    def testAdd(self):
        rTable = RoutingTable.RoutingTable('A')
        rTable.addRoute('C', 1.2, 'B')
        self.assertEqual(True, rTable.contains('C'))
        rTable.addRoute('D', 1.4, 'B')
        self.assertEqual(True, rTable.contains('D'))
        rTable.addRoute('E', 1.6, 'C')
        self.assertEqual(True, rTable.contains('E'))
        self.assertEqual(False, rTable.contains('F'))
        
    def testEdit(self):
        rTable = RoutingTable.RoutingTable('A')
        rTable.addRoute('C', 1.2, 'B')
        rTable.addRoute('D', 1.4, 'B')
        rTable.addRoute('E', 1.6, 'C')
        rTable.editRoute('C', 1.4, 'E')
        self.assertFalse(rTable.getVector('C').dist == 1.2)
        self.assertEqual(rTable.getVector('C').dist, 1.4)
        rTable.editRoute('D', 2.3, 'E')
        self.assertFalse(rTable.getVector('D').dist == 1.4)
        self.assertEqual(rTable.getVector('D').dist, 2.3)
        rTable.editRoute('E', 1.1, 'D')
        self.assertFalse(rTable.getVector('E').dist == 1.6)
        self.assertEqual(rTable.getVector('E').dist, 1.1)

    def testDel(self):
        rTable = RoutingTable.RoutingTable('A')
        rTable.addRoute('C', 1.2, 'B')
        rTable.addRoute('D', 1.4, 'B')
        rTable.addRoute('E', 1.6, 'C')
        #rTable.printTable()
        self.assertEqual(True, rTable.contains('C'))
        rTable.delRoute('C')
        self.assertFalse(rTable.contains('C'))
        rTable.delRoute('D')
        self.assertFalse(rTable.contains('D'))
        rTable.delRoute('E')
        self.assertFalse(rTable.contains('E'))
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()