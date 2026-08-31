from collections import deque

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # Here we are using BFS approach on a adjacency list

        # RULE 1: A perfect tree MUST have exactly one less connection (edge) than the number of dots (nodes). 
        # If it has more connections than that, it's mathematically guaranteed to have a circle (loop).
        if len(edges) > n - 1:
            return False

        # SETUP: Create a cheat sheet to track which dot is connected to which.
        # Imagine building a directory of who is neighbors with who.
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # TRACKER: We need a checklist to remember which dots we have already visited so we don't count them twice.
        visit = set()
        
        # WORKER: We make a waiting line to explore the dots. 
        # We start at dot '0'. The '-1' is just a fake placeholder meaning "we didn't come from anywhere yet."
        q = deque([(0, -1)])  # Structure is: (current dot, the dot we just came from)
        
        # Check off dot '0' on our list because we are starting there.
        visit.add(0)

        # EXPLORATION: Keep checking dots as long as our waiting line isn't empty.
        while q:
            node, parent = q.popleft()
            
            # Look at all the neighbors connected to the dot we are currently standing on.
            for nei in adj[node]:
                
                # If the neighbor is the dot we JUST walked away from, ignore it. 
                # We don't want to immediately turn around and walk back through the same door!
                if nei == parent:
                    continue
                    
                # BAD NEWS: If we bump into a neighbor that is ALREADY on our visited checklist,
                # it means we walked in a circle to get here! Trees are strictly not allowed to have circles.
                if nei in visit:
                    return False
                    
                # Add the newly discovered neighbor to our checklist.
                visit.add(nei)
                
                # Put the neighbor in the waiting line to check its connections later. 
                # (We pass 'node' as the parent so the neighbor knows where it came from).
                q.append((nei, node))

        # FINAL CHECK: Did our exploration actually reach every single dot?
        # If our checklist length equals 'n' (the total dots), it means everything is connected in one piece. (True)
        # If it doesn't match, it means some dots are stranded on a disconnected island. (False)
        return len(visit) == n