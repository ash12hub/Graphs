
def earliest_ancestor(ancestors, starting_node):
    children = {}
    for ancestor in ancestors:
        if ancestor[1] not in children:
            children[ancestor[1]] = set()
            children[ancestor[1]].add(ancestor[0])
        else:
            children[ancestor[1]].add(ancestor[0])

    visited = set()
    stack = []
    stack.append([starting_node])
    max_length = 1
    earliest = -1
    while len(stack) > 0:
        current_path = stack.pop()
        current_node = current_path[-1]

        if len(current_path) > max_length or len(current_path) == max_length and current_node < earliest:
            max_length = len(current_path)
            earliest = current_node

        if current_node not in visited:
            visited.add(current_node)
            if current_node in children:
                parents = children[current_node]
                for parent in parents:
                    parent_copy = current_path.copy()
                    parent_copy.append(parent)
                    stack.append(parent_copy)
    return earliest
