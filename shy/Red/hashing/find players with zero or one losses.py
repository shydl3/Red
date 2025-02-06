'''
given an integer array matches, where matches[i] = [winneri, loseri] indicates that
the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:
answer[0] is a list of all players that have not lost any matches.
answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.
'''

'''
Example 1:
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
'''



'''
use 3 hashing sets to store the players with 0-loss, 1-loss, and more-loss
update each time of iterating matches
'''

# use hashing sets:
# time complexity:
# for each iteration, O(1) to update the sets. totally O(n)
# finally it takes O(n logn) to sort the results
class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        # initialize hashing sets
        zero_loss = set()
        one_loss = set()
        more_losses = set()

        for winner, loser in matches:
            if (winner not in one_loss) and (winner not in more_losses):
                zero_loss.add(winner)

            if loser in zero_loss:
                zero_loss.remove(loser)
                one_loss.add(loser)

            elif loser in one_loss:
                one_loss.remove(loser)
                more_losses.add(loser)

            elif loser in more_losses:
                continue

            else:
                one_loss.add(loser)

        return [sorted(list(zero_loss)), sorted(list(one_loss))]


'''
use hashing map:
initialize a hashmap to track number of losses of each player
'''
# still O(nlogn)

class Solution2:
    def findWinner(self, matches):
        losses_count = {}

        # dict.get(key, default), 如果没有记录，返回默认0
        for winner, loser in matches:
            losses_count[winner] = losses_count.get(winner, 0)
            losses_count[loser] = losses_count.get(loser, 0) + 1

        zero_loss, one_loss = [], []

        # items() 是 Python 字典（dict）的一个内置方法
        # 返回一个包含字典所有键值对的 对象
        for player, count in losses_count.items():
            if count == 0:
                zero_loss.append(player)
            if count == 1:
                one_loss.append(player)

        return [sorted(zero_loss), sorted(one_loss)]

