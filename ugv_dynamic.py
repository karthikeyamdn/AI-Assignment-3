import heapq
import random

SIZE = 20
grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

start = (0, 0)
goal = (SIZE-1, SIZE-1)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar():
    pq = [(0, start)]
    cost = {start: 0}
    parent = {}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            return parent

        # Dynamic obstacle appears randomly
        x, y = random.randint(0, SIZE-1), random.randint(0, SIZE-1)
        grid[x][y] = 1

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0]+dx, current[1]+dy

            if 0 <= nx < SIZE and 0 <= ny < SIZE and grid[nx][ny] == 0:
                new_cost = cost[current] + 1
                if (nx, ny) not in cost or new_cost < cost[(nx, ny)]:
                    cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (priority, (nx, ny)))
                    parent[(nx, ny)] = current

    return None

parent = astar()

# reconstruct path
path = []
cur = goal
while cur in parent:
    path.append(cur)
    cur = parent[cur]
path.append(start)
path.reverse()

print("Dynamic Path:", path)
