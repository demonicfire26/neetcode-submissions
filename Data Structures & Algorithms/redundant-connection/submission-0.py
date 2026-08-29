class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        
        # 1. SETUP: Imagine every number is a person. 
        # We make a list where everyone starts as their own "boss".
        # We do len(edges) + 1 because the numbers start at 1, not 0.
        parent = [i for i in range(len(edges) + 1)]
        
        # 2. HELPER TOOL: A mini-function to find someone's ultimate, top-level boss.
        def find(node):
            # If the person is not their own boss, keep asking up the chain
            if parent[node] != node:
                parent[node] = find(parent[node])
            # Return the top boss
            return parent[node]

        # 3. MAIN WORK: Look at every connection (edge) one by one.
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            
            # Find the top boss for both people in this new connection
            root1 = find(node1)
            root2 = find(node2)
            
            # If they already have the exact same top boss, they are already in the same group!
            # Connecting them again creates a useless circle (a cycle). 
            # This is the bad connection we are looking for, so we return it.
            if root1 == root2:
                return edge
                
            # If they have different bosses, it's a valid new connection. 
            # We merge their groups together by making one boss report to the other.
            parent[root1] = root2
            
        return []