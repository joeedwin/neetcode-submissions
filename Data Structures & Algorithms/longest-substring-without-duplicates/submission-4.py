class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = set()
        i = 0
        templong = 0

        for j in range(len(s)):
            while s[j] in long:
                long.remove(s[i])
                i += 1

            long.add(s[j])
            templong = max(templong, len(long))

        return templong