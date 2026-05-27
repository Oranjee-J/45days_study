from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for ch in strs:
            key = ''.join(sorted(ch))
            if key not in group:
                group[key] = []
            
            group[key].append(ch)
        
        result = []
        for key in group:
            result.append(group[key])
        return result
    

s = Solution()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(s.groupAnagrams(strs))