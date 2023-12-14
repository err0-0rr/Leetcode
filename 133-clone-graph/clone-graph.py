"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        m={}
        done=set()
        visited=set() 
        q=deque()
        q.append(node)
        while q:
            a=q.popleft()
            if not a:
                continue
            if a.val not in m:
                m[a.val]=Node(a.val)
            if a.val not in done:
                for i in a.neighbors:
                    if i.val not in m:
                       m[i.val] =Node(i.val)
                    m[a.val].neighbors.append(m[i.val])
                done.add(a.val)
                
            for i in a.neighbors:
                if i not in visited:
                    visited.add(i)
                    q.append(i)
                
        return m[node.val]