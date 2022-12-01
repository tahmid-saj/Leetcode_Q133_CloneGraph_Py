"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        clones = {}
      
        def solve ( node ) :
            new_ = Node(node.val)   
            clones[node] = new_    
            
            for vertex in node.neighbors :
                if vertex in clones : 
                    new_.neighbors.append(clones[vertex])
                    
                else :                    
                    new_.neighbors.append(solve(vertex))
                    
            return new_
        
        if not node :
            return None
        
        return solve( node )
