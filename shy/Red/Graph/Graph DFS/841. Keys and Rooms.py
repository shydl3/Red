'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks,
and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i
return true if you can visit all the rooms, or false otherwise.

rooms = [[1],[2],[3],[]]
'''

class Solution(object):
    def solu(self, rooms: list[list[int]]) -> bool:
        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in rooms[node]:
                if not seen[neighbor]:
                    seen[neighbor] = True
                    stack.append(neighbor)
                # 给定的rooms列表可能重复房间。因此不能发现访问过直接return False
                # else:
                #     return False
        return all(seen)



    # 递归版本
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:

        def dfs(node):
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        seen = {0}
        dfs(0)
        return len(seen) == len(rooms)


    def iteration(self, rooms: list[list[int]]) -> bool:
        stack = []
        seen = {0}

        while stack:
            node = stack.pop()
            for neighbor in rooms[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return len(seen) == len(rooms)
