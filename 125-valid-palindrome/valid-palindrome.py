class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())        
        aux_str = ''
        for i in range(len(s)-1,-1,-1):
            aux_str += s[i]
        if aux_str == s:
            return True
        else:
            return  False