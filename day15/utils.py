"""
Utils used for both the Dijkstra's algorithm and A*.

Last update: 24/01/2022
"""


def get_neighbors(node: tuple, graph: dict) -> list:
    """
    Extract the neighbours of a node given the graph

    Args:
        node: Node of interest
        graph: Dictionary describing the graph

    Returns:
        List with all possible neighbours
    """

    result = []

    for idx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbor_coord_y = node[0] + idx[0]
        neighbor_coord_x = node[1] + idx[1]
        if 0 <= neighbor_coord_y and 0 <= neighbor_coord_x:
            if (neighbor_coord_y, neighbor_coord_x) in graph:
                result.append((neighbor_coord_y, neighbor_coord_x))
            else:
                continue

    return result
