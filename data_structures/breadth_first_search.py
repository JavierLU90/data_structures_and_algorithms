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
    
    def bfs_path(self, start, end):
        '''It takes a start vertex and an end vertex as inputs.
        It should return the shortest path between these two vertices in the self.graph as a list. 
        The list should include the start and end vertices and all the vertices in between.
        If a path is not found, return None.'''
        visited = []
        to_visit = [start]
        path = {start: None}
        while to_visit:
            current_vertex = to_visit.pop(0)
            visited.append(current_vertex)
            if current_vertex == end:
                path_list = []
                while current_vertex is not None:
                    path_list.append(current_vertex)
                    current_vertex = path[current_vertex]
                path_list.reverse()
                return path_list

            sorted_neighbors = sorted(self.graph[current_vertex])
            for neighbor in sorted_neighbors:
                if neighbor not in visited and neighbor not in to_visit:
                    to_visit.append(neighbor)
                    path[neighbor] = current_vertex
        return None


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