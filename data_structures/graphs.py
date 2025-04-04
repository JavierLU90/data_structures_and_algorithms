class Graph:
    ''' OLD CODE
    def __init__(self, num_vertices):
        #   Create a new data member called graph, it should be an empty list. Fill the graph with n lists, where n is the number of vertices in the graph. Each of these lists should contain n False values.
        self.graph = []
        for i in range(num_vertices):
            row = []
            for j in range(num_vertices):
                row.append(False)
            self.graph.append(row)

    def add_edge(self, u, v):
        #   It takes two vertices as inputs. It adds an edge to the graph by setting the corresponding cells to True.
        self.graph[u][v] = True
        self.graph[v][u] = True

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]'''
    
    def __init__(self):
        '''It should create an empty dictionary called graph as a data member.'''
        self.graph = {}

    def add_edge(self, u, v):
        '''It takes two vertices as inputs, and adds an edge to the adjacency list (the dictionary)'''
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

'''
GRAPHS

A graph is a set of vertices and the edges that connect those vertices. 
All trees are graphs, but not all graphs are trees.

For now, we'll use a matrix to represent the edges in a graph that connect each pair of vertices. 

	0	    1	    2	    3	    4
0	False	True	False	False	True
1	True	False	True	True	True
2	False	True	False	True	False
3	False	True	True	False	True
4	True	True	False	True	False

In Python, we can use a list of lists to represent this matrix:
[
  [False, True, False, False, True],
  [True, False, True, True, True],
  [False, True, False, True, False],
  [False, True, True, False, True],
  [True, True, False, True, False]
]

In any True cell the corresponding vertices are connected by an edge.

When an algorithm traverses a graph, it typically moves across the edges.


Common Use Cases
    Use Case	    Vertex	    Edge
    
    Social Networks	User	    Connection
    Road Maps	    Location	Road
    Networks	    Computer	Cable
    Game Dev	    Tile	Path
    AI Decision	    State	Action


Properties:
    Graphs can have any number of vertices.
    An undirected graph can have up to n(n - 1)/2 edges for n vertices.
    Vertices can exist without edges but may be disconnected (and thus kinda useless)
    Typically graphs (with the exception of multigraphs) can only have a single edge between two vertices
    Weighted graphs assign values (costs) to edges (we'll cover this in a future course)
'''