class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        curr=strs[0]
        for w in strs[1:]:
            g=''
            for i in range(min(len(curr),len(w))):
                if curr[i] == w[i]:
                    g=g+curr[i]
                else:
                    break
            curr=g  
        return curr
