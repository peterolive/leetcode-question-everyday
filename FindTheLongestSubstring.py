class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        c_m = [1, 0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0]
        max_ = 0
        mask = 0
        m = [-1] * 32
        for i in range(len(s)):
            mask ^= c_m[ord(s[i]) - ord('a')]
            if mask != 0 and m[mask] == -1:
                m[mask] = i
            max_ = max(max_, i - m[mask])
        return max_
