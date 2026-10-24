class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in seen :
                seen[sorted_word] = []

            seen[sorted_word].append(word)
        return list(seen.values())

sol = Solution()
anagram_list = sol.groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(anagram_list)

        