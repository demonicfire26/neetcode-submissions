from collections import defaultdict

class Solution:
    # Think of these numbers like sticky-note labels we put on each class to track our progress.
    WHITE = 1  # "Not started yet"
    GRAY = 2   # "Working on it right now"
    BLACK = 3  # "Completely finished and safe"

    def __init__(self):
        # We create placeholders for our tracking tools. 
        self.isPossible = True
        self.color = {}
        self.adjList = defaultdict(list)
        self.topologicalOrder = []

    def setup(self, numCourses):
        # Reset everything for a fresh start.
        self.isPossible = True
        self.color = {}
        self.adjList = defaultdict(list)
        self.topologicalOrder = []
        
        # Give every single class a "Not started yet" (WHITE) sticky note.
        for i in range(numCourses):
            self.color[i] = self.WHITE

    # This is our mini-worker function that explores the path starting from a specific class.
    def dfs(self, node):
        # If we already found out earlier that the schedule is impossible (we found a loop), 
        # stop working and go back.
        if not self.isPossible:
            return
        
        # We are actively checking this class now. 
        # Change its sticky note to "Working on it right now" (GRAY).
        self.color[node] = self.GRAY
        
        # Look at all the other classes that require THIS class to be done first.
        for neighbor in self.adjList[node]:
            # If the next class hasn't been touched yet, send our worker down that path.
            if self.color[neighbor] == self.WHITE:
                self.dfs(neighbor)
            
            # BAD NEWS: If the next class is ALSO marked "Working on it right now" (GRAY), 
            # it means we ran in a circle! (e.g., Class A needs B, and B needs A).
            elif self.color[neighbor] == self.GRAY:
                self.isPossible = False
                
        # We have successfully checked everything down this path.
        # Change this class's sticky note to "Completely finished" (BLACK).
        self.color[node] = self.BLACK
        
        # Add it to our final schedule list.
        self.topologicalOrder.append(node)

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Step 1: Prep our sticky notes and empty lists.
        self.setup(numCourses)
        
        # Step 2: Build a cheat sheet of connections.
        # If a rule is [0, 1], it means you take class 1 (src) to unlock class 0 (dest).
        for dest, src in prerequisites:
            self.adjList[src].append(dest)
            
        # Step 3: Go through every single class one by one.
        for i in range(numCourses):
            # If we haven't looked at it yet, start investigating it.
            if self.color[i] == self.WHITE:
                self.dfs(i)
                
        # Step 4: Hand in our final answer.
        if self.isPossible:
            # Because of how we dug down to the bottom of the paths and worked backwards, 
            # our final list is actually in reverse order. We flip it backwards ([::-1]) to fix it.
            return self.topologicalOrder[::-1]
        else:
            # We found a loop, so graduating is impossible. Return an empty list.
            return []