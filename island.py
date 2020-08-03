def dft_recursive(node, visited, islands):
    visited.add(node)

    neighbors = get_neighbors(node, islands)

    for neighbor in neighbors:
        if islands[node[0]][node[1]] == 1:
            dft_recursive(node, visited, islands)


def get_neighbors(node, islands):
    row, col = node
    neighbors = []

    # Check Left
    if row > 0:
        neighbors.append(row - 1, col)
    # Check Right
    if row < len(islands) - 1:
        neighbors.append(row + 1, col)
    # Check Up
    if col > 0:
        neighbors.append(row, col - 1)
    # Check Down
    if col < len(islands) - 1:
        neighbors.append(row, col + 1)
    return neighbors


def isalnds_counter(islands):
    total_islands = 0
    visited = set()

    for row in range(len(islands)):
        for columns in range(len(islands))
        node = (row, col)

        if islands[row][col] == 1 and node not in visited:
            total_islands += 1
            dft_recursive(node, visited)
