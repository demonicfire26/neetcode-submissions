from collections import deque

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        
        # Here we are using BFS approach on a adjacency list

        # 1. SETUP: Imagine 'n' is the number of people in a room.
        # We create a blank contact list for every single person.
        adj = [[] for _ in range(n)]
        
        # We also create a checklist to remember who we have already talked to.
        # 'False' means "I haven't met this person yet."
        visit = [False] * n
        
        # Fill out the contact list based on the given connections (edges).
        # If person 'u' is friends with person 'v', they both go in each other's contact lists.
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 2. THE WORKER: This function meets one person, and then goes on a mission 
        # to meet all of their friends, their friends' friends, and so on.
        def bfs(node):
            # Put the first person in a waiting line.
            q = deque([node])
            # Check them off so we don't count them twice.
            visit[node] = True
            
            # Keep working as long as there are people in the line.
            while q:
                cur = q.popleft() # Bring the next person to the front of the line.
                
                # Look at everyone in this person's contact list.
                for nei in adj[cur]:
                    # If we haven't met this friend yet...
                    if not visit[nei]:
                        # Check them off the list.
                        visit[nei] = True
                        # Put them in the waiting line so we can ask for THEIR friends later.
                        q.append(nei)

        # 3. THE MAIN MISSION
        res = 0  # This is our counter for how many disconnected friend groups exist.
        
        # Go through every single person in the room from 0 to n-1.
        for node in range(n):
            
            # If we stumble upon someone we haven't met yet...
            if not visit[node]:
                # We tell our worker to go meet them and EVERYONE connected to them.
                # Once the worker is done, everyone in that entire friend group will be checked off.
                bfs(node)
                
                # Because we found a totally new, unvisited person, it means we found a brand new group!
                res += 1
                
        # Return the final number of completely separate friend groups we counted.
        return res