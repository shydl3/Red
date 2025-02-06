'''
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''



'''
生成通配符字典 all_combo_dict
{
    "*ot": ["hot", "dot", "lot"],
    "h*t": ["hot"],
    "ho*": ["hot"],

    "d*t": ["dot"],
    "do*": ["dot", "dog"],
    "*og": ["dog", "log", "cog"],
    "d*g": ["dog"],

    "l*t": ["lot"],
    "lo*": ["lot", "log"],
    "l*g": ["log"],

    "c*g": ["cog"],
    "co*": ["cog"]
}
'''

from collections import deque
from collections import defaultdict

class Sulotion:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if (
            endWord not in wordList
            or not endWord
            or not beginWord
            or not wordList
        ):
            return 0

        n = len(beginWord)

        # 生成通配符字典 all_combo_dict
        # 作为后续bfs的相关搜索库
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(n):
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while queue:
            curr_word, steps = queue.popleft()
            # 对于当前的字符curr_word，遍历其可能的通配符模式inter_word （每个字母依次取星号）
            # 并继续遍历每个通配符模式在wordlist中对应的新单词（通过访问上一步的通配符字典 all_combo_dict实现）
            for i in range(n):
                inter_word = (curr_word[:i] + "*" + curr_word[i+1:])

                # 再对每个对应的新单词判断
                for word in all_combo_dict[inter_word]:
                    if word == endWord:
                        return steps + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, steps + 1))

                # all_combo_dict[inter_word] 存储所有符合该模式的单词。
                # 可能存在多个单词匹配相同的 inter_word
                # all_combo_dict[inter_word]遍历完后，没有找到endword则将其设置为空，避免后面重复访问。不影响结果但影响效率
                all_combo_dict[inter_word] = []
        return 0




