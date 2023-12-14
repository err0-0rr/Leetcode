class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ls=sentence.split()
        def util(s):
            if len(s)<len(searchWord):
                return False
            for i,j in zip(s, searchWord):
                if i!=j:
                    return False
            return True
            
        for i in range(len(ls)):
            if util(ls[i]):
                return i+1
        return -1