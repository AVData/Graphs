# pseudo code for the graph traversals; depth then breadth first

'''
Depth first:
_____________

push starting node on stack:

while stack isn't empty:
    pop the node off the top fo the stack
    if node isn't visited:
        visit the node (e.g. print it out)
        mark it as visited
        push all its neighbors on the stack


Breadth-First Traversal:
________________________

add starting node to queue

while queue isn't empty:
    take the node from the front of the queue
    if node isn't visited:
        visit the node (e.g. print it out)
        mark it as visited
        add all its neighbors to the queue


Graph Representations:
______________________

How we store the graph in memory

1. Adjacency Matrix
2. Adjacency List

A matrix is a grid

  A B C D E F G H
A   T   T       T
B T   T
C   T         T
D T
E
F
G     T
H T
'''
