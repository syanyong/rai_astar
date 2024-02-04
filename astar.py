import heapq


def heuristic(a, b):
  return abs(b[0] - a[0]) + abs(b[1] - a[1])


def search(grid, start, goal):
  neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  close_set = set()
  came_from = {}
  gscore = {start: 0}
  fscore = {start: heuristic(start, goal)}
  open_set = []

  heapq.heappush(open_set, (fscore[start], start))

  while open_set:
    current = heapq.heappop(open_set)[1]

    if current == goal:
      data = []
      while current in came_from:
        data.append(current)
        current = came_from[current]
      return data

    close_set.add(current)
    for i, j in neighbors:
      neighbor = current[0] + i, current[1] + j
      tentative_g_score = gscore[current] + heuristic(current, neighbor)
      if 0 <= neighbor[0] < grid.shape[0]:
        if 0 <= neighbor[1] < grid.shape[1]:
          if grid[neighbor[0]][neighbor[1]] == 1:
            continue
        else:
          continue
      else:
        continue

      if neighbor in close_set and tentative_g_score >= gscore.get(
          neighbor, 0):
        continue

      if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [
          i[1] for i in open_set
      ]:
        came_from[neighbor] = current
        gscore[neighbor] = tentative_g_score
        fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
        heapq.heappush(open_set, (fscore[neighbor], neighbor))

  return False


def print_path_in_grid(grid, path):
  # Create a copy of the grid so the original grid isn't altered
  grid_copy = [row[:] for row in grid]

  # Mark the path on the grid
  for x, y in path:
    grid_copy[x][y] = 9

  # Print the grid with the path
  for row in grid_copy:
    print(' '.join(str(cell) for cell in row))

  return grid_copy
