# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 23:47:13 2019

@author: mi
"""
import Graph

class DFS():
    
    def __init__(self, g):
        self._g = g
        self._visited = [False for _ in range(g.v())]
        self._res = []
        
        for v in range(g.v()):
            if not self._visited[v]:
                self._dfs(v)
        
    def _dfs(self, v):
        self._visited[v] = True
        self._res.append(v)
        
        for u in self._g.adj(v):
            if not self._visited[u]:
                self._dfs(u)
        
    def res(self):
        return self._res
        
if __name__ == "__main__":
    
    g = Graph.Graph("g.txt")
    dfs = DFS(g)
    print(dfs.res())
    