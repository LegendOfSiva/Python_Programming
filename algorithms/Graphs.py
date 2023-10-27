import heapq


class WeightedGraph:
    def __init__(self):
        self.Glist = {}

    def __str__(self):
        result = ""
        for vertex in self.Glist:
            result += f"{vertex} : {self.Glist[vertex]} \n"
        return result

    def add_vertex(self, vertex):
        if vertex not in self.Glist:
            self.Glist[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 in self.Glist and vertex2 in self.Glist:
            self.Glist[vertex1].append((vertex2, weight))
            self.Glist[vertex2].append((vertex1, weight))

    def remove_vertex(self, vertex):
        if vertex in self.Glist:
            for adjacent_vertex in self.Glist[vertex]:
                self.Glist[adjacent_vertex[0]].remove((vertex, adjacent_vertex[1]))
            self.Glist.pop(vertex)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.Glist and vertex2 in self.Glist:
            self.Glist[vertex1] = [
                (v, w) for v, w in self.Glist[vertex1] if v != vertex2
            ]
            self.Glist[vertex2] = [
                (v, w) for v, w in self.Glist[vertex2] if v != vertex1
            ]

    def dfs_recursive(self, start_vertex):
        visited = set()

        def recursive(vertex):
            visited.add(vertex)
            print(vertex, end=" ")
            for neighbour, _ in self.Glist[vertex]:
                if neighbour not in visited:
                    recursive(neighbour)

        recursive(start_vertex)

    def dfs_iterative(self, vertex):
        vertices = set()
        stack = [vertex]
        while stack:
            current_node = stack.pop()
            if current_node not in vertices:
                vertices.add(current_node)
                print(current_node, end=" ")
            for neighbour, _ in self.Glist[current_node]:
                if neighbour not in vertices:
                    stack.append(neighbour)

    """BFS is same as DFS , but instead of using a stack , we will use a Queue like queue=[vertex] and pop from 
    beginning like current_node=queue.pop(0)"""

    def dijkstra(self, start_vertex):
        distances = {vertex: float('inf') for vertex in self.Glist}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.Glist[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


g = WeightedGraph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_vertex("D")
g.add_vertex("E")

g.add_edge("A", "B", 2)
g.add_edge("A", "C", 1)
g.add_edge("B", "D", 3)
g.add_edge("C", "E", 4)

print("\nDFS Recursive starting from vertex 'A':")
g.dfs_recursive("A")
print("\n_________________\nDFS Iterative starting from vertex A")
g.dfs_iterative("A")
print("\n_____Graph_____\n")
print(g)
print("\nDijkstra's Algorithm starting from vertex 'A':")
distances = g.dijkstra("A")
for vertex, distance in distances.items():
    print(f"Distance from A to {vertex}: {distance}")