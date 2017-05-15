'''
Created on Oct 27, 2015

@author: Avery
'''

class Triple:
    '''
    The triple class, which holds the distance, destination, and first hop of an element on the routingTable
    '''
    
    dist = None
    dest = None
    first_hop = None
    

    def __init__(self, dest,dist, first_hop):
        '''
        Constructor
        '''
        self.dest = dest
        self.dist = dist
        self.first_hop = first_hop
    
        
    
    