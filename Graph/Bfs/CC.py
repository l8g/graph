# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:03:23 2019

@author: mi
"""


import sys
sys.path.insert(0, '..Expression')

from Graph import Graph
from collections import deque

class CC():
    
    def __init__(self, g):
        self._g = g
        self._visited = [False] * g.v()
        self._cccount = 0
        
        for v in range(g.v()):
            if not self._visited[v]:
                self._bfs(v)
                self._cccount += 1
                
    def _bfs(self, v):
        queue = deque()
        self._visited[v] = True
        queue.append(v)
        
        while len(queue) > 0:
            curr = queue.popleft()
            for w in self._g.adj(curr):
                if not self._visited[w]:
                    self._visited[w] = True
                    queue.append(w)
        
    def count(self):
        return self._cccount
    
if __name__ == "__main__":
    g = Graph("g.txt")
    cc = CC(g)
    print(cc.count())
    
    g = Graph("g2.txt")
    cc = CC(g)
    print(cc.count())
    
    g = Graph("g3.txt")
    cc = CC(g)
    print(cc.count())






