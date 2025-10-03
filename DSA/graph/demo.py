class Graph:
    '''
    This is easy, really. There are two steps you can do this with adjacency lists:
    1. Add a vertex: This means creating am entry in the adjacency list, key would be the node itself, value will be an empty list
    2. Connect the vertex: if vertex exists, take the value of the vertex from the list, add the connecting pair to it's list, do the same with the other element in the pair (add v1 in v2's, and vice versa)
    '''
    def __init__ (self):
        # This is our adjacency list
        self.lst = {}
    
    def add_new (self, vertex):
        '''
        if vertex is not there in self.lst, add it, if not then don't bother.
        '''
        if vertex not in self.lst:
            self.lst[vertex] = []
        else:
            raise Exception("DuplicateFound: The vertex already exists")
    
    def add_edges(self, v1, v2):
        '''
        Connect the two vertices, add to each other
        '''

        # if the vertices don't exist, add them
        if v1 not in self.lst:
            self.lst[v1] = []
        if v2 not in self.lst:
            self.lst[v2] = []
        
        # two vertices, add them to each other's lists. This does not check for duplicate edges though, be careful
        self.lst[v1].append(v2)
        self.lst[v2].append(v1)
    
    def dfs(self, start):
        '''
        what is dfs, exactly?
        it is a traversal technique- you can use it for searching by checking the results manually, it has nothing to do with searching directly like you'd imagine.
        How does this work?
        Simply pass it a start value- note how there is no root in graphs? Yeah, which is why you can pass any vertex, and scan from *that* vertex.
        What does this have to do with paths? 
        This is a recursive technique, that tracks adjacency lists, in an undirectional graph, it may not show things in path.

        For example, say you have this kind of graph: [B] ---- [A] ---- [C]
        The adjacency list for that would look like this:
        {
        "A" : ["B", "C"],
        "B" : ["A"],
        "C" : ["A"]
        }

        If you start at A, dfs does this:

        1. It will add A to a set called 'visited' and print it, if it is not there already- if it is there, the function ends there
        2. Then, it will iterate through A's list (i.e. B and C), first B:
            a. B is passed back to dfs
            b. if B is not in visited, you add it- here, you added it to visited and printed it too
            c. it will now iterate through B's list (i.e. A), so:
                i. A is passed back to dfs
                ii. A is visited, so this function ends -> kill stack
            d. now, onto next of B's list- but wait, there isn't one -> kill stack
        3. Notice the visited set now, it looks like this: {A, B}
        4. Now, do it with C, same way:
            a. C is passed back to dfs
            b. if C is not in visited, you add it- here, you added it to visited and printed it too
            c. it will now iterate through C's list (i.e. A), so:
                i. A is passed back to dfs
                ii. A is visited, so this function ends -> kill stack
            d. now, onto next of C's list- but wait, there isn't one -> kill stack
        5. A's list ended, nothing more to iterate -> kill stack
        6. you get final visited set as: {A, B, C}

        Notice how the stack gives no idea about the actual sequence or path, if you go with what it suggests, you would read that as: A --- B --- C, which is incorrect, yeah?

        So path != traversal, nor is dfs != searching algo
        '''

        # implementing that in code:
        visited = set()

        def _dfs(vertex):
            # just so we are sure
            if vertex not in self.lst:
                raise Exception("VertexNotFound: No Vertex found in the adjacency list, add one, dumbass")
            

            if vertex not in visited:
                # if vertex is not already visited:
                # print vertex
                print(vertex)
                # add this in visited
                visited.add(vertex)

                # this is the for loop that checks for each point of adjacency list
                for neighbor in self.lst[vertex]:
                    # so grab each vertex's adjacent peeps, which are their neighbor, add if they are not visited, ignore if visited
                    _dfs(neighbor)
        
        _dfs(start)
        print(visited)

    def bfs(self, start):
        '''
        What is BFS, exactly?
        BFS = Breadth-First Search. It's a traversal technique, like DFS, but instead of diving deep first, it explores all neighbors of a vertex level by level. 
        Pass a start vertex, and BFS will scan all reachable nodes systematically.

        How does it work?
        - BFS uses a queue to track which vertex to visit next.
        - BFS guarantees you visit vertices in "layers" (distance from start), unlike DFS which dives deep.


        Example graph:
            [B] ---- [A] ---- [C]
                    |
                    [D]

        Adjacency list:
        {
            "A": ["B", "C", "D"],
            "B": ["A"],
            "C": ["A"],
            "D": ["A"]
        }

        BFS starting from A does this:
        1. Initialize visited set = {A}, queue = [A]
        2. Pop A from queue, visit neighbors B, C, D
        - Add B, C, D to visited, enqueue them: queue = [B, C, D]
        3. Pop B from queue, visit neighbors (A)
        - A already visited, ignore
        4. Pop C from queue, visit neighbors (A)
        - Already visited, ignore
        5. Pop D from queue, visit neighbors (A)
        - Already visited, ignore
        6. Queue empty -> traversal done
        Final visited set: {A, B, C, D}

        Notice: BFS gives you the “level order” of nodes. 
        Path reconstruction? Not done automatically—BFS alone is traversal.

        Notes / Extra insights:
        1. You can import inside a function. Here we import deque inside BFS for cleanliness, and because we only need it here.
        2. Why a queue and not a stack?
            - Using a stack would turn BFS into DFS.
            - Think about it, if you add a neigbor of neighbor, and it were a stack, you'd pop the neighbor, so the traversal happens like a string of firecrackers, it goes on bursting, with queue, the algo steps back to the origin, checks other neighbors as we pop them
            - BFS = level-order traversal. Queue ensures we finish all nodes of a layer before moving deeper.
            - Stack would immediately dive deep, skipping the “layered” property.
        3. Neighbor-of-neighbor logic:
            - Only enqueue if not already visited. Otherwise, we'd revisit nodes endlessly.
            - Queue preserves the layer-order; stack would break it.
            - This ensures BFS doesn't go deep like a recursive rabbit hole; it systematically explores layer by layer.
        '''


        from collections import deque

        visited = set([start])
        queue = deque([start])

        print("BFS starting from", start)
        while queue:
            # this loop basically goes on until the queue is empty- when the queue is empty, that would mean all are visited- ...
            # pop the queue, load it in vertex
            vertex = queue.popleft()  # pop from front of queue

            # just so we are sure
            if vertex not in self.lst:
                raise Exception("VertexNotFound: No Vertex found in the adjacency list, add one, dumbass")
            

            print(vertex)             # visit the vertex

            # iterate through the neigbors of each vertex, if not visited, visit them, add them to the queue- then pop the queue in the next, bigger iteration of the queue. 
            # Now the queue grows as it scans the neihbors, if visited, the loop breaks, next adds, since its a queue, the visited remains in the front, the non-visited never get added. The ones which do get added, they are not popped immediately, the neighbors are popped and organized.
            for neighbor in self.lst[vertex]:
                # no recursion here, just if they are not there in visited, add them to the queue, and add it to visited, otherwise ignore
                if neighbor not in visited:
                    visited.add(neighbor)  # mark as visited
                    queue.append(neighbor) # enqueue for next visit

        print("Visited set:", visited)

                

    def show(self):
        # a simple printing statement that tells you what happens
        for vertex in self.lst:
            print(f"{vertex} -> {self.lst[vertex]}")

string = "ABCDEF"
gr = Graph()

for s in range(len(string)):
    if s+1 < len(string):
        gr.add_edges(string[s], string[s+1])
# gr.add_edges("A", "")

gr.dfs("A")
gr.bfs("A")
gr.show()

# The above gives same answer for visited set because the input is literally a straight line 🧍‍♂️