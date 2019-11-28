# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 00:09:12 2019

@author: mi
"""

from collections import deque
import Graph

class BFS():
    
    def __init__(self, g):
        self._g = g
        self._visited = [False for _ in range(g.v())]
        self._res = []
        
        for u in range(g.v()):
            if not self._visited[u]:
                self._bfs(u)
    
    def _bfs(self, u):
        queue = deque()
        queue.append(u)
        self._visited[u] = True
        
        while len(queue) > 0:
            curr = queue.popleft()
            self._res.append(curr)
            
            for v in self._g.adj(curr):
                if not self._visited[v]:
                    queue.append(v)
                    self._visited[v] = True
                    
    def res(self):
        return self._res
    

if __name__ == "__main__":
    g = Graph.Graph("g.txt")
    bfs = BFS(g)
    print(bfs.res())