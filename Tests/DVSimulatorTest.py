'''
Created on Oct 27, 2015

@author: Avery
'''
import unittest
import DVSimulator


class Test(unittest.TestCase):


    def testDistance(self):
        simulator = DVSimulator.DVSimulator("network.txt")
        simulator.printRouters()
        self.assertEqual(simulator.dist('A', 'B'), 2.1)
        self.assertEqual(simulator.dist('A', 'D'), float('inf'))
        self.assertEqual(simulator.dist('B', 'B'), 0)
        self.assertEqual(simulator.dist('B', 'C'), 1.2)
        self.assertEqual(simulator.dist('C', 'B'), 1.2)
        self.assertEqual(simulator.dist('C', 'D'), 1.5)

    def testSimulation(self):
        simulator = DVSimulator.DVSimulator("network.txt")
        simulator.printRouters()
        simulator.runSimulation()
        self.assertEqual(simulator.dist('A', 'B'), 2.1)
        self.assertEqual(simulator.dist('A', 'D'), 2.5)
        self.assertEqual(simulator.dist('B', 'B'), 0)
        self.assertEqual(simulator.dist('B', 'C'), 1.2)
        self.assertEqual(simulator.dist('C', 'B'), 1.2)
        self.assertEqual(simulator.dist('C', 'D'), 1.5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()