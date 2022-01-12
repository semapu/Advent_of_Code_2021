"""
Description:

    Now, big caves can be visited any number of times, a single small cave can be visited at most twice, and the
    remaining small caves can be visited at most once. However, the caves named start and end can only be visited
    exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave,
    the path must end immediately.

    Now, input_simple.txt has 36 possible paths.

Goal:
    How many paths through this cave system are there?

"""

import numpy as np
import pandas as pd

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

# ========= #
# Functions #
# ========= #

# ================= #
# Deep-first search #

def deep_first_search(edges, node, visited):
    """
    Pseudocode:

        procedure DFS(G, v) is
            label v as discovered
            for all directed edges from v to w that are in G.adjacentEdges(v) do
                if vertex w is not labeled as discovered then
                    recursively call DFS(G, w)

    Args:
        edges: edges defining the graph
        node: current node to study
        visited: already visited nodes in the current path

    Returns:
        A recursive implementation of DFS:[5]
    """

    # Initialize the result
    paths = []

    # Set the new node as visited
    new_visit = visited + [node]

    # Check if end of the graph
    if node == 'end':
        return [new_visit]
    #  if it is not a terminal node, continue exploration
    for n in edges[node]:
        # Ensure "start" is only visited one time
        if n != 'start':
            # Big caves can be visited many times
            if n.isupper():
                temp_result = deep_first_search(edges, n, new_visit)
                paths.extend(temp_result)
            # Only one small cave can be visited twice
            else:
                # extract all the small cave in the current path
                small_visited_caves = [i for i in new_visit if i.islower()]
                # check if any small cave has been visited twice
                twice = any([True for i in small_visited_caves if small_visited_caves.count(i) > 1])
                # continue exploration if one small cave visited twice and "n" is the first time, or
                # continue exploration if no small cave visited twice, and is the second time visiting "n"
                if (twice and new_visit.count(n) == 0) or (not twice and new_visit.count(n) < 2):
                    temp_res = deep_first_search(edges, n, new_visit)
                    paths.extend(temp_res)
    return paths
# ================= #


# ==== #
# Main #
# ==== #


if __name__ == '__main__':

    # ================== #
    # Preprocessing data #
    # ================== #

    # Store the edges of the graph. They are bidirectional.
    edges = dict()

    # Read the input data
    line = file.readline()
    while line != "":
        nodes = line.strip().split("-")

        # Check if node seen previously
        if nodes[0] in edges:
            edges[nodes[0]].append(nodes[1])
        #  else, add the new node
        else:
            edges[nodes[0]] = [nodes[1]]
        if nodes[1] in edges:
            edges[nodes[1]].append(nodes[0])
        else:
            edges[nodes[1]] = [nodes[0]]

        line = file.readline().strip()

    # Close the file
    file.close()

    # Traversing graph data structure, from "start" to "end"
    paths_graph = deep_first_search(edges, 'start', [])

    # ================ #
    # Print the result #
    # ================ #

    print("Result {}: {}".format("deep_first_search", len(paths_graph)))

    aux = 1

    


