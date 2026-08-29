"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        # We are using the DFS approach for this problem using adjacency list

        # We are making a new hahmap to keep a track of nodes that we have visited or not
        visited = {}

        # Checking if the given 'node' is null
        if not node:
            return node
        
        # Create a nested helper function for the recursion
        def dfs(curr_node):
            # If we have already visited the existing node, return its value
            if curr_node in visited:
                return visited[curr_node]

            # Create the clone of the existing node and immediately store it in visited
            cloneNode = Node(curr_node.val, [])
            visited[curr_node] = cloneNode        

            # Recursively clone all neighbors using the helper function
            for neighbor in curr_node.neighbors:
                 cloneNode.neighbors.append(dfs(neighbor))
                 
            return cloneNode

        # Trigger the DFS
        return dfs(node)





