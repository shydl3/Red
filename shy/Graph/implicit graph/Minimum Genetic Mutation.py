from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        queue = deque([(startGene, 0)])

        seen = {startGene}

        while queue:
            node, steps = queue.popleft()
            if node == endGene:
                return steps

            for c in "ACGT":
                for i in range(len(node)):
                    neighbor = node[:i] + c + node[i+1:]
                    if neighbor in bank and neighbor not in seen:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)

        return -1


