'''
Created on Oct 27, 2015

@author: Avery
'''
import RoutingTable
import Triple

class DVRouter:
    '''
    classdocs
    '''
    rTable = None
    name = None
    links = {}
    splitHorizonOn = False;

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.rTable = RoutingTable.RoutingTable(name)
        self.links = {}
        self.addLink(name, 0)
        self.splitHorizonOn = False
        
    def export(self):
        return self.rTable
    
    def rimport(self,neighborTables):
        returnValue = False
        
        for neighborTable in neighborTables:
            #If neighborTable name is not a neighbor, skip it
            if neighborTable.name in self.links: 
                #Update the current table using neighborTable and Distance Vector protocol
                for vector in neighborTable.vector_list:
                    #Check to see if the vector is already contained in the table. If so, check to see whether this path is faster
                    vectorDist = vector.dist+self.rTable.getVector(neighborTable.name).dist
                    if self.rTable.contains(vector.dest):
                        if vectorDist < self.rTable.getVector(vector.dest).dist:
                            self.rTable.editRoute(vector.dest, vectorDist, neighborTable.name)
                            returnValue = True
                    else:
                        self.rTable.addRoute(vector.dest, vectorDist, neighborTable.name)
                        returnValue = True
        return returnValue
                    
    def addLink(self, routerName, dist):
        #Adds a link to the router's list of links
        self.links[routerName] = dist
        self.rTable.addRoute(routerName, dist, routerName)
        
    def removeLink(self, routerName):
        #removes a link from the router's list of links
        del self.links[routerName]
        v =self.rTable.getVector(routerName)
        if v.first_hop == routerName:
            #If this is a direct link, we need to delete it from our routing table as well
            self.rTable.delRoute(routerName)
            
    def printTable(self):
        #Prints a router's routing table
        self.rTable.printTable()
        
    def printTableToX(self, x):
        #Prints a router's routing table links that go to router named X
        self.rTable.printTableToX(x)
        