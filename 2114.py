class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxSpaceCount = 0
        for i in range(len(sentences)):
            currSpaceCount = sentences[i].count(" ")
            if currSpaceCount > maxSpaceCount:
                maxSpaceCount = currSpaceCount
            currSpaceCount = 0
        return maxSpaceCount + 1
            
        
