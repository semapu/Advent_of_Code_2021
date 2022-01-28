# Search algorithms: Blind and Heuristic 

Path-ﬁnding algorithms come in two main varieties: those in which the goal plays an active role in the
search, and those in which the goal sits passively until encountered.

The standard way in which goals can bias the search is by means of heuristic functions ; these are functions h(s) that 
provide a quick-and-dirty estimate of the cost to reach the goal from the state s , making the search goal-directed.

Uniform Cost Search, also called **Dijkstra’s algorithm**, is a **brute force** or **blind algorithm**.

**A*** uses a **heuristic** to direct the search.

## Dijkstra's algorithm

Dijkstra’s algorithm is a popular search algorithm used to determine the shortest path between two nodes in a graph.

Algorithm: 

    Let the node at which we are starting be called the initial node. Let the distance of node Y be the distance from 
    the initial node to Y. Dijkstra's algorithm will initially start with infinite distances and will try to improve them 
    step by step.

        1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
        
        2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all 
        other nodes. The tentative distance of a node v is the length of the shortest path discovered so far between the node v 
        and the starting node. Since initially no path is known to any other vertex than the source itself (which is a path 
        of length zero), all other tentative distances are initially set to infinity. Set the initial node as current.

        3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances through 
        the current node. Compare the newly calculated tentative distance to the current assigned value and assign the 
        smaller one. For example, if the current node A is marked with a distance of 6, and the edge connecting it with
        a neighbor B has length 2, then the distance to B through A will be 6 + 2 = 8. If B was previously marked with a
        distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
        
        4. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited 
        and remove it from the unvisited set. A visited node will never be checked again.

        5. If the destination node has been marked visited (when planning a route between two specific nodes) or if the 
        smallest tentative distance among the nodes in the unvisited set is infinity (when planning a complete traversal; 
        occurs when there is no connection between the initial node and remaining unvisited nodes), then stop. 
        The algorithm has finished.
        
        6. Otherwise, select the unvisited node that is marked with the smallest tentative distance, 
        set it as the new current node, and go back to step 3.

    When planning a route, it is actually not necessary to wait until the destination node is "visited" as above: 
    the algorithm can stop once the destination node has the smallest tentative distance among all "unvisited" nodes 
    (and thus could be selected as the next "current"). 


## A*

A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: 
starting from a specific starting node of a graph, it aims to find a path to the given goal node having the smallest cost

At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of 
the path and an **estimate** of the **cost required to extend the path all the way to the goal**. Specifically, A* selects the 
path that minimizes.

    f(n) = g(n) + h(n)

    1. g(n) is the cost of the path from the start node to n,
    2. h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal.

Typical implementations of A* use a priority queue to perform the repeated selection of minimum (estimated) cost nodes to expand. 

At each step of the algorithm, the node with the lowest f(x) value is removed from the queue, the f and g values of its
neighbors are updated accordingly, and these neighbors are added to the queue. The algorithm continues until a removed
node (thus the node with the lowest f value out of all fringe nodes) is a goal node.

As an example, when searching for the shortest route on a map, h(x) might represent the straight-line distance to the 
goal, since that is physically the smallest possible distance between any two points. For a grid map from a video game,
using the Manhattan distance.

    1: Firstly, Place the starting node into OPEN and find its f (n) value.

    2: Then remove the node from OPEN, having the smallest f (n) value. If it is a goal node, then stop and return 
        to success.
    
    3: Else remove the node from OPEN, and find all its successors.
    
    4: Find the f (n) value of all the successors, place them into OPEN, and place the removed node into CLOSE.
    
    5: Goto Step-2.
    
    6: Exit.

## Reference

### Dijkstra's algorithm
Wikipedia: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Using_a_priority_queue

### A*

TO BE DONE ...