import networkx as nx
import pylab

class Board(object):
    def __init__(self):
        self.G = nx.Graph()
        self.cities = ['Atlanta',        'Boston',         'Calgary',
                        'Charleston',    'Chicago',        'Dallas',     
                        'Denver',        'Duluth',         'El Paso',
                        'Helena',        'Houston',        'Kansas City', 
                        'Las Vegas',     'Little Rock',    'Los Angeles', 
                        'Miami',         'Montreal',       'Nashville',
                        'New Orleans',   'New York',       'Oklahoma City',
                        'Omaha',         'Phoenix',        'Pittsburgh',
                        'Portland',      'Raleigh',        'Saint Louis', 
                        'Salt Lake City','San Francisco',  'Santa Fe',
                        'Sault St Marie','Seattle',        'Toronto', 
                        'Vancouver',     'Washington',     'Winnipeg'
                        ]

        for city in self.cities:
            self.G.add_node(city)

        ##possible edge colors: red,     orange,     yellow, 
        #                       green,   blue,       purple, 
        #                       black,   white,      grey

        self.G.add_edge('Vancouver', 'Seattle', 
                        weight = 1, 
                        edgeColors = ['grey', 'grey'])
                        
        self.G.add_edge('Vancouver', 'Calgary', 
                        weight = 3, 
                        edgeColors = ['grey'])
                        
        self.G.add_edge('Calgary', 'Seattle', 
                        weight = 4, 
                        edgeColors = ['grey'])
                        
        self.G.add_edge('Calgary', 'Winnipeg', 
                        weight = 6, 
                        edgeColors = ['white'])
                        
        self.G.add_edge('Calgary', 'Helena', 
                        weight = 4, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Helena', 'Seattle', 
                        weight = 6, 
                        edgeColors = ['yellow'])
        
        self.G.add_edge('Portland', 'Seattle', 
                        weight = 1, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Portland', 'San Francisco', 
                        weight = 5, 
                        edgeColors = ['green', 'purple'])
        
        self.G.add_edge('Portland', 'Salt Lake City', 
                        weight = 6, 
                        edgeColors = ['blue'])
        
        self.G.add_edge('Salt Lake City', 'San Francisco', 
                        weight = 5, 
                        edgeColors = ['orange', 'white'])
        
        self.G.add_edge('Los Angeles', 'San Francisco', 
                        weight = 3, 
                        edgeColors = ['yellow', 'purple'])
        
        self.G.add_edge('Los Angeles', 'Las Vegas', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Los Angeles', 'Phoenix', 
                        weight = 3, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Las Vegas', 'Salt Lake City', 
                        weight = 3, 
                        edgeColors = ['orange'])
        
        self.G.add_edge('Salt Lake City', 'Helena', 
                        weight = 3, 
                        edgeColors = ['purple'])
        
        self.G.add_edge('Helena', 'Winnipeg', 
                        weight = 4, 
                        edgeColors = ['blue'])
        
        self.G.add_edge('Helena', 'Denver', 
                        weight = 4, 
                        edgeColors = ['green'])
        
        self.G.add_edge('Salt Lake City', 'Denver', 
                        weight = 3, 
                        edgeColors = ['red', 'yellow'])
        
        self.G.add_edge('Phoenix', 'Santa Fe', 
                        weight = 3, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Los Angeles', 'El Paso', 
                        weight = 6, 
                        edgeColors = ['black'])
        
        self.G.add_edge('Phoenix', 'El Paso', 
                        weight = 3, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('El Paso', 'Santa Fe', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Santa Fe', 'Denver', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Helena', 'Duluth', 
                        weight = 6, 
                        edgeColors = ['orange'])
        
        self.G.add_edge('Helena', 'Omaha', 
                        weight = 5, 
                        edgeColors = ['red'])
        
        self.G.add_edge('Winnipeg', 'Duluth', 
                        weight = 4, 
                        edgeColors = ['black'])
        
        self.G.add_edge('Winnipeg', 'Sault St Marie', 
                        weight = 6, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Denver', 'Omaha', 
                        weight = 4, 
                        edgeColors = ['purple'])
        
        self.G.add_edge('Denver', 'Kansas City', 
                        weight = 4, 
                        edgeColors = ['black', 'orange'])
        
        self.G.add_edge('Denver', 'Oklahoma City', 
                        weight = 4, 
                        edgeColors = ['red'])
        
        self.G.add_edge('Santa Fe', 'Oklahoma City', 
                        weight = 3, 
                        edgeColors = ['blue'])
        
        self.G.add_edge('El Paso', 'Oklahoma City', 
                        weight = 5, 
                        edgeColors = ['yellow'])
        
        self.G.add_edge('El Paso', 'Dallas', 
                        weight = 4, 
                        edgeColors = ['red'])
        
        self.G.add_edge('El Paso', 'Houston', 
                        weight = 6, 
                        edgeColors = ['green'])
        
        self.G.add_edge('Houston', 'Dallas', 
                        weight = 1, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Dallas', 'Oklahoma City', 
                        weight = 2, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Oklahoma City', 'Kansas City', 
                        weight = 2, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Omaha', 'Kansas City', 
                        weight = 1, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Omaha', 'Duluth', 
                        weight = 2, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Duluth', 'Sault St Marie', 
                        weight = 3, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Duluth', 'Toronto', 
                        weight = 6, 
                        edgeColors = ['purple'])
        
        self.G.add_edge('Duluth', 'Chicago', 
                        weight = 3, 
                        edgeColors = ['red'])
        
        self.G.add_edge('Omaha', 'Chicago', 
                        weight = 4, 
                        edgeColors = ['blue'])
        
        self.G.add_edge('Dallas', 'Little Rock', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Oklahoma City', 'Little Rock', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Houston', 'New Orleans', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('New Orleans', 'Little Rock', 
                        weight = 3, 
                        edgeColors = ['green'])
        
        self.G.add_edge('Little Rock', 'Saint Louis', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Kansas City', 'Saint Louis', 
                        weight = 2, 
                        edgeColors = ['blue', 'purple'])
        
        self.G.add_edge('Little Rock', 'Nashville', 
                        weight = 3, 
                        edgeColors = ['white'])
        
        self.G.add_edge('Nashville', 'Saint Louis', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Saint Louis', 'Chicago', 
                        weight = 2, 
                        edgeColors = ['green', 'white'])
        
        self.G.add_edge('Sault St Marie', 'Toronto', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Sault St Marie', 'Montreal', 
                        weight = 5, 
                        edgeColors = ['black'])
        
        self.G.add_edge('Montreal', 'Toronto', 
                        weight = 3, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Montreal', 'Boston', 
                        weight = 2, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Montreal', 'New York', 
                        weight = 3, 
                        edgeColors = ['blue'])
        
        self.G.add_edge('Toronto', 'Pittsburgh', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Toronto', 'Chicago', 
                        weight = 4, 
                        edgeColors = ['white'])
        
        self.G.add_edge('Boston', 'New York', 
                        weight = 2, 
                        edgeColors = ['yellow', 'red'])
        
        self.G.add_edge('New York', 'Pittsburgh', 
                        weight = 2, 
                        edgeColors = ['green', 'white'])
        
        self.G.add_edge('New York', 'Washington', 
                        weight = 2, 
                        edgeColors = ['orange', 'black'])
        
        self.G.add_edge('Pittsburgh', 'Chicago', 
                        weight = 3, 
                        edgeColors = ['orange', 'black'])
        
        self.G.add_edge('Pittsburgh', 'Saint Louis', 
                        weight = 5, 
                        edgeColors = ['green'])
        
        self.G.add_edge('Pittsburgh', 'Nashville', 
                        weight = 4, 
                        edgeColors = ['yellow'])
        
        self.G.add_edge('Pittsburgh', 'Raleigh', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Pittsburgh', 'Washington', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Washington', 'Raleigh', 
                        weight = 2, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Raleigh', 'Nashville', 
                        weight = 3, 
                        edgeColors = ['black'])
        
        self.G.add_edge('Nashville', 'Atlanta', 
                        weight = 1, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Atlanta', 'Raleigh', 
                        weight = 2, 
                        edgeColors = ['grey', 'grey'])
        
        self.G.add_edge('Raleigh', 'Charleston', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Atlanta', 'New Orleans', 
                        weight = 4, 
                        edgeColors = ['yellow', 'orange'])
        
        self.G.add_edge('Atlanta', 'Charleston', 
                        weight = 2, 
                        edgeColors = ['grey'])
        
        self.G.add_edge('Miami', 'Charleston', 
                        weight = 4, 
                        edgeColors = ['purple'])
        
        self.G.add_edge('Miami', 'Atlanta', 
                        weight = 5, 
                        edgeColors = ['blue'])
        
        self.G.add_edge('Miami', 'New Orleans', 
                        weight = 6, 
                        edgeColors = ['red'])
    
        #create a copy of the board to store the original state of the board
        self.copyBoard = self.G.copy()
        
    def showBoard(self, board, pauseTime = 7):
        """display board
        """
        pos=nx.spring_layout(board)
        nx.draw(board, pos)
        nx.draw_networkx_edge_labels(board, pos)
        pylab.ion()
        pylab.show()
        pylab.pause(pauseTime)
        pylab.close()
    
    def hasEdge(self, city1, city2):
        """returns True an edge exists between city1, city2.  False otherwise
        city1, city2: string
        """
        return self.G.has_edge(city1, city2)

    def removeEdge(self, city1, city2, edgeColor):
        """remove the edge between two cities that's colored edgeColor
        city1, city2:  string
        edgeColor:  string
        raises ValueError if edge does not exist
        """
        if not self.hasEdge(city1, city2):
            raise ValueError("Edge between %s and %s does not exist" 
                                % (city1, city2))
        
        posColors = self.getEdgeColors(city1, city2)
        
        #if the edge is grey, accept any color and remove grey
        if "grey" in posColors:
            self.G.get_edge_data(city1, city2)['edgeColors'].remove("grey")
            if len(self.G.get_edge_data(city1, city2)['edgeColors']) == 0:
                self.G.remove_edge(city1, city2)
            
        else:
            if edgeColor not in posColors:
                raise ValueError("A %s edge does not exist between %s and %s" 
                                    % (edgeColor, city1, city2))
            
            #if edge has a color, remove that color
            self.G.get_edge_data(city1, city2)['edgeColors'].remove(edgeColor)
            if len(self.G.get_edge_data(city1, city2)['edgeColors']) == 0:
                self.G.remove_edge(city1, city2)
            
    def getEdges(self):
        """returns a list of tuples of all remaining edges', [(city1, city2)]
        """
        return self.G.edges()

    def getEdgeColors(self, city1, city2):
        """returns the edgeColors of edge
        city1, city2: string
        """
        return self.G.get_edge_data(city1, city2)['edgeColors']

    def getEdgeWeight(self, city1, city2):
        """returns the weight of the edge (i.e. the distance between two cities)
        city1, city2: string
        """
        return self.G.get_edge_data(city1, city2)['weight']
    
    def getPathWeight(self, city1, city2):
        """returns the weight of the shortest path between city1, city2
        """
        return nx.dijkstra_path_length(self.G, city1, city2)
    
    def getNodes(self):
        return self.G.nodes()

    def getCities(self):
        """returns a list of all remaining cities
        that can be traveled to or from
        """
        return self.G.nodes()
    
    def getAdjCities(self, city1):
        """returns a list of cities adjacent to city1 
        that still have available edges
        """
        return [x[1] for x in self.G.edges(city1)]
        
    def hasPath(self, city1, city2):
        """returns True if a path exists between city1 and city2
        searches self.G (the graph the class uses)
        city1, city2: String
        """
        return nx.has_path(self.G, city1, city2)
    
    def iterEdges(self):
        """returns an interator over all edges and edge data"""
        return self.G.edges_iter(data = True)
        
class PlayerBoard(Board):
    """Creates a custom graph for each player to represent their progress"""
    def __init__(self):
        self.G = nx.Graph()
    
    def addEdge(self, city1, city2, routeDist, color):
        """
        city1, city2, color: Strings
        routeDist          : int
        """
        self.G.add_edge(city1, city2, weight = routeDist, edgeColors = [color])

    def longestPath(self, start):
        """returns a tuple: (len longestPath, tuple of cities along longestPath)
        This is a modification of BFS that uses edges instead of nodes
        It has no ending condition, rather it searches the whole graph and
        returns the weight of the longest path and the edges that of that path

        #Doctest

        >>> p = PlayerBoard()
        >>> p.addEdge('a', 'b', 1, 'blue')
        >>> p.addEdge('b', 'd', 1, 'blue')
        >>> p.addEdge('d', 'e', 1, 'blue')
        >>> p.addEdge('e', 'f', 98, 'blue')
        >>> p.addEdge('e', 'b', 1, 'blue')
        >>> p.addEdge('b', 'c', 1, 'blue')
        >>> p.addEdge('a', 'z', 1, 'blue')
        
        >>> p.longestPath('b')
        (100, (['b', 'd', 'e', 'f'], set([('d', 'e'), ('e', 'f'), ('b', 'd')])))
        
        # if p.addEdge('e', 'f', 1, 'blue')
        # (5, (['b', 'd', 'e', 'b', 'a', 'z'], \
        #    set([('b', 'a'), ('d', 'e'), ('a', 'z'), ('e', 'b'), ('b', 'd')])))

        """
        
        longestPath = (0, ())
        q = []
        
        q.append( ([start], set()) ) #( [path], set(exploredEdges) )
        
        while q:
            cur = q.pop() #pop() = DFS, pop(0) = BFS (consider Deque for O(1))
            
            if len(cur[1]) > 0:
                pathWeight = sum( [self.getEdgeWeight(x[0],x[1]) 
                                    for x in cur[1]] )
            
                if pathWeight > longestPath[0]:
                    longestPath = (pathWeight, cur)
            
            node = cur[0][-1]
            edgesExplored = cur[1]
            adjCities = set()
            for i in self.getAdjCities(node):
                #add if edge between cities not explored
                if (node, i) not in edgesExplored:
                    if (i, node) not in edgesExplored:
                        adjCities.add(i) 
            
            for suc in adjCities:
                proxy = cur[1].copy()
                proxy.add((node, suc))
                newPath = cur[0] + [suc]

                q.append((newPath, proxy)) #add to path, add edge
                    
        
        #Note: set of path edges will not be ordered
        return longestPath        

if __name__ == "__main__":
    import doctest
    doctest.testmod()