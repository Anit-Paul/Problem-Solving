from collections import defaultdict,deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        wordList=set(wordList)
        wordList.add(beginWord)

        graph=defaultdict(list)

        #creation of the graph with possible patterns
        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+'*'+word[i+1:]
                graph[pattern].append(word)
        
        #bfs traversal
        q=deque()
        q.append((beginWord,1))
        visit=set()
        visit.add(beginWord)
        while q:
            word,dist=q.popleft()
            for i in range(len(word)):
                pattern=word[:i]+'*'+word[i+1:]
                for j in graph[pattern]:
                    if(j==endWord):
                        return dist+1
                    if(j not in visit):
                        visit.add(j)
                        q.append((j,dist+1))
        
        return 0
