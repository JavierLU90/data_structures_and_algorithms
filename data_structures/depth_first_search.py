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
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        '''It takes a list of vertices that have been visited so far and a current vertex as input.
        Visits neighbors recursively calling itself with the neighboring vertex.'''
        visited.append(current_vertex)
        sorted_neighbors = sorted(self.graph[current_vertex])
        for neighbor in sorted_neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)


'''
DEPTH FIRST SEARCH

Depth-first search (DFS) is just another algorithm to traverse a graph - kind of like breadth first search. 
It starts at a root node (some arbitrary node on the graph) and explores as far as possible along each branch before backtracking and starting down the next branch.

So, should you use DFS or BFS when traversing a graph? Well, it depends. 
Let's look at some rules of thumb we can use to help make the decision.

Is the Solution Close to the Root?
If you have a good reason to believe the vertex you're looking for is close to the root (where you plan to start searching) then BFS should be faster.

Does the Graph Have Wide Levels?
Imagine a tree-like graph with 10 vertices on the first level. 
Each of those ten vertices point to another ten vertices. 
The number of vertices at each level would be:
    level 0: 1
    level 1: 10
    level 2: 100
    level 3: 1000
    level 4: 10000
Because BFS stores each horizontal level in memory at the same time, you might run out of memory. 
DFS would likely be more memory efficient.

Is the Search Space Infinite?
In some searches, the graph has infinite size. For example, imagine a simulation of a game of chess.

The first level of the graph represents all the possible current moves, 
the next level all the possible 2nd moves, and this goes on forever, 
especially when you consider that there are possible loops within the game 
(moving a queen back and forth).

In these cases, true DFS is practically impossible, you would either be forced to:
    Use BFS
    Use another algorithm
    Put a limit on how far your DFS algorithm can search before returning
'''