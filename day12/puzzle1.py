"""
Description:

    The only way to know if you've found the best path is to find all of them.

    Fortunately, the sensors are still mostly working, and so you build a rough map of the remaining caves
    (your puzzle input). For example:
        start-A
        start-b
        A-c
        A-b
        b-d
        A-end
        b-end

    This is a list of how all of the caves are connected. You start in the cave named start,
    and your destination is the cave named end. An entry like b-d means that cave b is connected to cave d -
    that is, you can move between them.

    So, the above cave system looks roughly like this:
            start
            /   \
        c--A-----b--d
            \   /
             end

Goal:
    Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves
    more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves
    (written in lowercase, like b).

    All paths you find should visit small caves at most once, and can visit big caves any number of times.

    Given these rules, there are 10 paths through this example cave system:
        start,A,b,A,c,A,end
        start,A,b,A,end
        start,A,b,end
        start,A,c,A,b,A,end
        start,A,c,A,b,end
        start,A,c,A,end
        start,A,end
        start,b,A,c,A,end
        start,b,A,end
        start,b,end

"""

import numpy as np
import pandas as pd
from collections import defaultdict

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
        if n != 'start':
            if n not in visited or n.isupper():
                temp_result = deep_first_search(edges, n, new_visit)
                paths.extend(temp_result)
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


    


