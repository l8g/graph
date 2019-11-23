

class Graph():
    
    def __init__(self, fileName):
        f = open(fileName, "rt")
        s = f.read()
        f.close()
        
        lines = s.splitlines()
        ve = lines[0].split()
        self._v = int(ve[0])
        e = int(ve[1])
        
        self._edges = [set() for _ in range(self._v)]
        self._e = 0
        
        
        for i in range(e):
            edge = lines[i+1].split()
            self.addEdge(int(edge[0]), int(edge[1]))
    
    def v(self):
        return self._v
    
    def e(self):
        return self._e
            
    def addEdge(self, u, v):
        self._e += 1
        self._edges[u].add(v)
        self._edges[v].add(u)
    
    def adj(self, v):
        return iter(self._edges[v])
        
    def hasEdge(self, u, v):
        return v in self._edges[u]
    
    def validate(self, u):
        assert u < self._v
    
    def __str__(self):
        return str([[v for v in s] for s in self._edges])

    

if __name__ == "__main__":
    g = Graph("g.txt")
    [print(v) for v in g.adj(1)]