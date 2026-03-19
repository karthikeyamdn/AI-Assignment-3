import csv
import heapq

def load_graph(filename):
    graph = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            city1, city2, dist = row[0], row[1], int(row[2])
            graph.setdefault(city1, []).append((city2, dist))
            graph.setdefault(city2, []).append((city1, dist))
    return graph

def dijkstra(graph, start, goal):
    pq = [(0, start)]
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    parent = {}

    while pq:
        current_dist, node = heapq.heappop(pq)

        if node == goal:
            break

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = parent[cur]
    path.append(start)
    path.reverse()

    return path, dist[goal]

# Example usage
graph = load_graph("indiancities_throughroads.csv")
start = input("Enter start city: ")
goal = input("Enter goal city: ")

path, cost = dijkstra(graph, start, goal)

print("Shortest Path:", path)
print("Total Distance:", cost)
