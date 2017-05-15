'''
Created on Oct 27, 2015

@author: Avery
'''
import Triple
class RoutingTable(object):
    '''
    Table to hold the distance vectors. Each Router will have a RoutingTable
    '''
    #dictionary holding list of vectors
    vector_list = []
    name = ""
    def __init__(self, name):
        self.vector_list = []
        self.name = name
    
    def addRoute(self, dest, length, firstHop):
        #Adds the route to the routing table
        v = Triple.Triple(dest, length, firstHop)
        self.vector_list.append(v)
    
    def delRoute(self, dest):
        #Delets a route from the routing table
        try:
            v = self.getVector(dest)
            self.vector_list.remove(v)
        except:
            raise ValueError("Not in List")
    
    def editRoute(self, dest, length, firstHop): 
        #Edits a route in the routing table   
        v = self.getVector(dest)
        v.dist = length
        v.first_hop = firstHop
        
    def contains(self, dest):
        #checks to see whether the table contains a route
        for vector in self.vector_list:
            #If the vector's name is the correct name, return true. It is contained in the list
            if vector.dest == dest:
                return True
        return False
    
    def getVector(self, dest):
        #returns a specified vector from the list
        for vector in self.vector_list:
            #If the vector's name is the correct name, return the vector
            if vector.dest == dest:
                return vector
        return None
    def printTable(self):
        #prints the table
        for vector in self.vector_list:
            #print the data of the vector
            print(vector.dest +" "+ str(vector.dist)+" "+ vector.first_hop)
            
    def printTableToX(self, x):
        #prints the table links that go to router named X
        for vector in self.vector_list:
            #print the data of the vector if its dest is X
            if vector.dest == x:
                print(vector.dest +" "+ str(vector.dist)+" "+ vector.first_hop)