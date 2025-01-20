class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        counter = 0

        if needle not in haystack or len(needle) > len(haystack):
            return -1

        else:
            for i in range(len(haystack)):
                if needle[0] == haystack[i]:
                    for j in range(i,len(haystack)):
                        if haystack[j] == needle[counter]:
                            counter += 1
                            if counter == len(needle):
                                return i
                        else:
                            counter = 0
                            break

                
                
