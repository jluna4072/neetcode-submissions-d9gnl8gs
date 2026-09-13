'''

'''
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        adj = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                temp = list(word)
                temp[i] = '.'
                temp = "".join(temp)
                adj[temp].append(word)
        
        res = 0
        q = deque()
        q.append(beginWord)
        visited = set()

        while q:
            
            for _ in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res + 1
                
                if word in visited:
                    continue

                for i in range(len(word)):
                    temp = list(word)
                    temp[i] = '.'
                    temp = "".join(temp)
                    for neigh in adj[temp]:
                        if neigh == word:
                            continue
                        q.append(neigh)
                visited.add(word)
            res+= 1
        return 0




        