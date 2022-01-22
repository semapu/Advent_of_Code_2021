"""
Description:
    The cavern is large, but has a very low ceiling, restricting your motion to two dimensions.
    The shape of the cavern resembles a square; a quick scan of chiton density produces a map of risk level throughout
    the cave (your puzzle input). For example:

        1163751742
        1381373672
        2136511328
        3694931569
        7463417111
        1319128137
        1359912421
        3125421639
        1293138521
        2311944581

Goal:

    You start in the top left position, your destination is the bottom right position, and you cannot move diagonally.
    The number at each position is its risk level; to determine the total risk of an entire path, add up the risk levels
    of each position you enter (that is, don't count the risk level of your starting position unless you enter it;
    leaving it adds no risk to your total).

Notes:
    The best implementation for this problem is to use Dijkstra's algorithm or A*.

    In this case, I am going to implement the Dijkstra's algorithm:
        It is an algorithm for finding the shortest paths between nodes in a graph.

        Dijkstra's original algorithm found the shortest path between two given nodes,[6] but a more common variant
        fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the
        graph, producing a shortest-path tree.

    A* achieves better performance by using heuristics to guide its search.
"""

import numpy as np
import pandas as pd
import math

# ========= #
# Functions #
# ========= #


def open_file(path: str):
    
    file = open(path)
    
    return file


def read_file_as_data_frame(path: str):
    
    inputs = pd.read_csv(path, sep="\n", skiprows=-1, dtype=str)
        
    return inputs
  

# =================== #
# Read the input data #
# =================== #

# Open the file conventionally,
file = open_file('./input.txt')
#  read the entire file,
# inputs = file.read()
#  read the next line.
# line = file.readline()

# Read the entire file as a DataFrame
# inputs = read_file_as_data_frame("./input.txt")

# ========== #
# Parameters #
# ========== #

starting_node = (0, 0)

# ======= #
# Helpers #
# ======= #


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


# ==== #
# Main #
# ==== #


if __name__ == '__main__':

    # =============== #
    # Read input data #
    # =============== #

    # Convert input data into a list of lists.
    grid = []

    line = file.readline()
    while line != '\n':
        grid.append([int(risk) for risk in line.strip()])
        line = file.readline()

    # Previous lines equivalent to the following ones
    # with open('input.txt') as f:
    #     grid = [[int(risk) for risk in line.strip()] for line in f]

    # Close the file
    file.close()

    # Set the end node
    end_node = (len(grid), len(grid[0]))

    # Dijkstra's algorithm

    # 1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
    unvisited_set = {}  # (node): tentative_distance
    visited_set = {}  # (node): distance

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
    # the current node. Compare the newly calculated tentative distance to the current assigned value and assign the
    # smaller one.
    while unvisited_set:
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

    # ================ #
    # Print the result #
    # ================ #

    print("Result: {}".format(visited_set[end_node]))
    

    


