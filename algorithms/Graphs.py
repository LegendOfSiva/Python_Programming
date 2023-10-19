class Graph:
    def __init__(self) -> None:
        self.Glist = {}

    def __str__(self):
        result = ""
        for vertex in self.Glist:
            result += f"{vertex} : {self.Glist[vertex]} \n"
        return result

    def add_vertex(self, vertex):
        if vertex not in self.Glist:
            self.Glist[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.Glist and vertex2 in self.Glist:
            self.Glist[vertex1].append(vertex2)
            self.Glist[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.Glist:
            for adjacent_vertex in self.Glist[vertex]:
                self.Glist[adjacent_vertex].remove(vertex)
            self.Glist.pop(vertex)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.Glist and vertex2 in self.Glist:
            self.Glist[vertex1].remove(vertex2)
            self.Glist[vertex2].remove(vertex1)

    def DFS_recursive(self, start_vertex):
        visited = set()

        def recursive(vertex):
            visited.add(vertex)
            print(vertex, end=" ")
            for neighbour in self.Glist[vertex]:
                if neighbour not in visited:
                    recursive(neighbour)

        recursive(start_vertex)

    def DFS_iterative(self, vertex):
        vertices = set()
        stack = [vertex]
        while stack:
            current_node = stack.pop()
            if current_node not in vertices:
                vertices.add(current_node)
                print(current_node, end=" ")
            for neighbour in self.Glist[current_node]:
                if neighbour not in vertices:
                    stack.append(neighbour)

    """BFS is same as DFS , but instead of using a stack , we will use a Queue like queue=[vertex] and pop from begining like current_node=queue.pop(0) """


g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")

print("\nDFS Recursive starting from vertex 'A':")
g.DFS_recursive("A")
print("\n_________________\nDFS Iterative starting from vertex A")
g.DFS_iterative("A")
