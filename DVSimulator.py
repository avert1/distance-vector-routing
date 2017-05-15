'''
Created on Oct 27, 2015

@author: Avery
'''
import DVRouter
import argparse
import sys
from _ast import arg
class DVSimulator:
    '''
    The simulator, which is in charge of keeping a map of the network and running the program
    '''
    f = None
    routers = []
    split = False
    use_dest = False
    dest = 'A'
    def __init__(self, fileName):
        self.routers = []
        self.split = False
        use_dest = False
        self.dest = 'A'
        self.f = open(fileName, mode='r')
        for line in self.f:
            #Split the line and create the links based on the information in the file
            info = line.split()
            if self.containsRouter(info[0]) ==False:
                new_router = DVRouter.DVRouter(info[0])
                self.routers.append(new_router)
            if self.containsRouter(info[1]) ==False:
                new_router = DVRouter.DVRouter(info[1])
                self.routers.append(new_router)
            for router in self.routers:
                #if we get the router we want to add to, create a new vector and add it to the router
                if router.name == info[0]:
                    router.addLink(info[1], float(info[2]))
                elif router.name == info[1]:
                    router.addLink(info[0], float(info[2]))
     
    def runSimulation(self):
        #Runs the simulation until the routers converge
        shouldRunAgain = True
        iteration = 1
        while shouldRunAgain:
            print("Iteration "+ str(iteration))
            iteration+=1
            shouldRunAgain =False
            routerTables = self.collectTables()
            for router in self.routers:
                if router.rimport(routerTables) == True:
                    shouldRunAgain = True
            self.printRouters()
        
        
    def collectTables(self):
        #collects the tables from each router
        routerTables = []
        for router in self.routers:
            #Add the exported routing table to the list
            routerTables.append(router.export())
        return routerTables
    
    def containsRouter(self,name):
        #Checks to see whether routers contains a router
        for router in self.routers:
            #If the router's name is the correct name, return true. It is contained in the list
            if router.name == name:
                return True
        return False
    
    def getRouter(self, name):
        #Gets a specified router
        for router in self.routers:
            #If the router's name is the correct name, return it
            if router.name == name:
                return router
        return None
    
    def dist(self, x, y):
        #Gets total distance from one router to the other. Returns infinity if no route is available
        router = self.getRouter(x)
        if router.export().contains(y):
            return float(router.export().getVector(y).dist)
        else:
            return float('inf')
        
    def printRouters(self):
        for router in self.routers:
            print("Router: "+router.name)
            router.printTable()
            
    def printRoutersToX(self, x):
        for router in self.routers:
            print("Router: "+router.name)
            router.printTableToX(x)
if __name__ == '__main__':
    #Create a new simulator and run the simulation
    simulator = DVSimulator("network.txt")
    for arg in sys.argv:
        #check to see if the argument specifies to split
        if arg[0] =='--':
            arg = arg[2:]
            if arg == "split":
                print("Using split horizon")
                simulator.split = True;
            elif '=' in arg:
                argList = arg.split('=')
                if argList[0] == "dest" and argList.length==3:
                    simulator.dest = argList[2]
                    print("Using dest")
                    simulator.use_dest = True
    simulator.runSimulation()