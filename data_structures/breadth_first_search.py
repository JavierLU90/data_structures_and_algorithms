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
    
    def breadth_first_search(self, v):
        '''This method traverses a graph level by level starting from a specified vertex, 
        and returns all vertices in the order they were visited. 
        The breadth-first approach ensures we explore all vertices at the current distance from the start 
        before moving further away.'''
        visited = []
        to_visit = [v]
        while to_visit:
            s = to_visit.pop(0)
            visited.append(s)
            sorted_neighbors = sorted(self.graph[s])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
        return visited


'''
BREADTH FIRST SEARCH

Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. 
It starts at a root (some arbitrary node on a graph), and explores all of the neighbor nodes at the present depth before going on to the nodes at the next level.


Stable Sorting

Non-integer sets are not "stable" in Python - the order of elements in a set is not guaranteed to be the same each time you iterate over it.

While testing, we want our algorithm to search the same way every time to make debugging easier. 
Python offers a sorted() function we can call on our set() that will return a sorted iterable.
    sorted_items = sorted(unsorted_set)

'''