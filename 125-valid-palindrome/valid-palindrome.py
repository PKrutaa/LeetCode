class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())        
        aux_str = ''
        for i in range(len(s)-1,-1,-1):
            print(i)
            print(s[i])
            aux_str += s[i]
        print(s)
        print(aux_str)
        if aux_str == s:
            return True
        else:
            return  False