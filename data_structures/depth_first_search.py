class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
    
    def depth_first_search(self, start_vertex):
        '''It takes a start vertex as input and traverses the graph in a depth-first manner and 
        record the vertices it visits in a list and returns it.'''
        pass

    def depth_first_search_r(self, visited, current_vertex):
        '''It takes a list of vertices that have been visited so far and a current vertex as input.
        Visits neighbors recursively calling itself with the neighboring vertex.'''
        pass


'''
DEPTH FIRST SEARCH

Depth-first search (DFS) is just another algorithm to traverse a graph - kind of like breadth first search. 
It starts at a root node (some arbitrary node on the graph) and explores as far as possible along each branch before backtracking and starting down the next branch.


'''