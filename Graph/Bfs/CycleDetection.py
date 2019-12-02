# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:22:29 2019

@author: mi
"""

import sys
sys.path.insert(0, "..Expression")

from Graph import Graph
from collections import deque

class CycleDetection():
    
    def __init__(self, g):
        self._g = g
        self._visited = [False] * g.v()
        self._parent = [-1] * g.v()
        
        self._hasCycle = False
        
        for v in range(g.v()):
            if not self._visited[v]:
                if self._bfs(v):
                    self._hasCycle = True
                    break
                
    def _bfs(self, v):
        queue = deque()
        self._visited[v] = True
        self._parent[v] = v
        queue.append(v)
        while len(queue) > 0:
            curr = queue.popleft()
            for w in self._g.adj(curr):
                if not self._visited[w]:
                    self._visited[w] = True
                    self._parent[w] = curr
                    queue.append(w)
                elif w != self._parent[curr]:
                    return True
        
        return False
    
    def hasCycle(self):
        return self._hasCycle
    
if __name__ == "__main__":
    g = Graph("g.txt")
    cd = CycleDetection(g)
    print(cd.hasCycle())
    
    g = Graph("g2.txt")
    cd = CycleDetection(g)
    print(cd.hasCycle())
    
    g = Graph("g3.txt")
    cd = CycleDetection(g)
    print(cd.hasCycle())
    
    
    
    
    
    
    
    