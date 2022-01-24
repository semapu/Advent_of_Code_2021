"""
Implementation Dijkstra's algorithm only using Dictionaries.
The implementation is really useful to understand the algorithm, but using
a Priority Queue should improve the performance (see implementation A*).

Last update: 24/01/2022
"""

import math
from utils import get_neighbors


def dijkstra_algorith(grid, starting_node, end_node):
    # ==================== #
    # Dijkstra's algorithm #
    # ==================== #

    # 1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
    unvisited_set = {}  # (node): tentative_distance
    visited_set = {}  # (node): smallest distance from starting node

    # 2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all
    #    other nodes. The tentative distance of a node v is the length of the shortest path discovered so far between
    #    the node v and the starting node.
    for y in range(len(grid)):
        row = grid[y]
        for x in range(len(row)):
            if (y, x) == starting_node:
                unvisited_set[(y, x)] = 0
            else:
                unvisited_set[(y, x)] = math.inf
    # 2. Set the initial node as current.
    current_node = (0, 0)

    # 3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through
    #    the current node. Compare the newly calculated tentative distance to the current assigned value and assign the
    #    smaller one.
    while unvisited_set:
        if len(unvisited_set) % 10000 == 0:
            print(len(unvisited_set))
        neighbors = get_neighbors(current_node, unvisited_set)

        for (new_y, new_x) in neighbors:
            tentative_distance = unvisited_set[current_node] + grid[new_y][new_x]

            if tentative_distance < unvisited_set[(new_y, new_x)]:
                unvisited_set[(new_y, new_x)] = tentative_distance

        # 4. When we are done considering all of the unvisited neighbors of the current node, mark the current node
        #    as visited and remove it from the unvisited set. A visited node will never be checked again.
        visited_set[current_node] = unvisited_set[current_node]
        del unvisited_set[current_node]

        # 5. If the destination node has been marked visited (when planning a route between two specific nodes)
        if end_node in visited_set:
            break

        # 6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the
        #    new current node, and go back to step 3.
        current_node = min(unvisited_set, key=unvisited_set.get)

    return visited_set
