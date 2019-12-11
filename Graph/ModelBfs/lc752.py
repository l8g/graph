from collections import deque
class Solution:
    def openLock(self, deadends, target: str) -> int:
        self._deadends = set(deadends)
        if target in self._deadends:
            return -1;
        if "0000" in self._deadends:
            return -1;
        if target == "0000":
            return 0;

        self._visited = dict()
        self._target = target
        self._bfs("0000")
        

        if target in self._visited:
            return self._visited[target]
        return -1

    def _bfs(self, s):
        self._visited[s] = 0
        queue = deque()
        queue.append(s)

        while len(queue) > 0:
            curr = queue.popleft()
            nexts = self._getNexts(curr)
            for n in nexts:
                if n not in self._visited and n not in self._deadends:
                    self._visited[n] = self._visited[curr] + 1
                    queue.append(n)
                    if n == self._target:
                        return
    
                    
    def _getNexts(self, s):
        nexts = list()
        for i in range(4):
            v  = int(s[i])
            n1 = s[:i] + str((v+1)%10) + s[i+1:]
            n2 = s[:i] + str((v+9)%10) + s[i+1:]
            nexts.append(n1);
            nexts.append(n2);
        return nexts

s = Solution()
print(s.openLock(["0201","0101","0102","1212","2002"], "0202"))