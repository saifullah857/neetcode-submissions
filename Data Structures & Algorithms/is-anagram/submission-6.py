class Solution:
    def isAnagram(self ,word1 , word2):
        if len(word1) != len(word2):
            return False
        return sorted(word1) == sorted(word2)
sol = Solution()
status = sol.isAnagram("maam" , "aamm")
print(status)

  