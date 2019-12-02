# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:53:48 2019

@author: mi
"""

from collections import deque
class Solution:
    def isBipartite(self, graph) -> bool:
        self._g = graph
        V = len(graph)
        
        self._visited = [False] * V
        self._colors = [0] * V
        for v in range(V):
            if not self._visited[v]:
                if not self._bfs(v):
                    return False
        return True
   
    def _bfs(self, v):
        queue = deque()
        self._visited[v] = True
        queue.append(v)
        
        while len(queue) > 0:
            curr = queue.popleft()
            for w in self._g[curr]:
                