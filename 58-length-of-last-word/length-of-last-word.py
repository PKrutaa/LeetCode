class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s) - 1
        while True:
            if ' ' in s:
                if s[i] == ' ' and count == 0:
                    i -= 1
                    continue
                elif s[i] == ' ':
                    break
                else:
                    count += 1
                    i -= 1
            else:
                return len(s)
        return count
