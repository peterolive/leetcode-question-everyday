class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = 0
        res = 0
        count_map = {c: 0 for c in 'abc'}
        for right in range(len(s)):
            count_map[s[right]] += 1
            while all(count_map.values()):
                count_map[s[left]] -= 1
                left += 1
            res += left

        return res
