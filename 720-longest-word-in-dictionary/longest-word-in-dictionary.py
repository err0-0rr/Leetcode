class Solution:
    def longestWord(self, words: List[str]) -> str:
        w=set(words)
        
        def util(s):
            t=''
            for i in s:
                t+=i
                if t not in w:
                    return False
            return True
            
        words.sort(key=lambda x:(-len(x), x))
        
        for i in words:
            if util(i):
                return i
        return ""