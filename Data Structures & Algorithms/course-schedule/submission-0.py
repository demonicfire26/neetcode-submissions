class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        # 1. SETUP THE CHEAT SHEET
        # We use a dictionary to map out the connections. 
        # Think of it like a list saying: "If you take Class A, it connects to Class B."
        courseGraph = {}
        
        # Loop through every pair of rules we are given
        for pre in prerequisites:
            # pre[1] is our starting class, pre[0] is the class connected to it
            # If the starting class is already in our dictionary, add to its list
            if pre[1] in courseGraph:
                courseGraph[pre[1]].append(pre[0])
            # If it's not in the dictionary yet, create a new list for it
            else:
                courseGraph[pre[1]] = [pre[0]]
                
        # 2. TRACKER FOR CIRCLES
        # We need a way to remember which classes we are actively looking at right now.
        # If we see the same class twice while following a path, we are stuck in an impossible loop!
        visited = set()
        
        # 3. MINI-WORKER (HELPER FUNCTION)
        # This function checks a single class to see if it leads to a dead-end circle.
        def courseSchedule(course, visited, courseGraph):
            
            # BAD NEWS: We just bumped into a class we are already checking. 
            # This means we ran in a circle. Return False (we can't finish).
            if course in visited:
                return False
                
            # GOOD NEWS: This class isn't in our cheat sheet (has no connections), 
            # or we already proved it was safe earlier. Return True (it's safe).
            if courseGraph.get(course) is None:
                return True
                
            # We are now actively checking this class, so add it to our tracker.
            visited.add(course)
            
            # Go through every connected class tied to this one
            for next_course in courseGraph.get(course):
                # Ask the mini-worker to check the next class. 
                # If it finds a circle down the line, everything fails.
                if courseSchedule(next_course, visited, courseGraph) == False:
                    return False
                    
            # We successfully checked all connections without getting stuck!
            # Take this class off the active tracker since we are done looking at it.
            visited.remove(course)
            
            # TRICK: Mark this class's connections as 'None' in the dictionary.
            # This saves time! If we stumble on this class again later, we instantly know it's safe.
            courseGraph[course] = None
            
            # The class is totally safe.
            return True

        # 4. MAIN TEST
        # Let's test every single class from 0 up to (numCourses - 1)
        for currentCourse in range(numCourses):
            # If our mini-worker ever finds a loop, we instantly fail the whole thing.
            if courseSchedule(currentCourse, visited, courseGraph) == False:
                return False
                
        # If we checked every single class and never found a circle, we can finish!
        return True