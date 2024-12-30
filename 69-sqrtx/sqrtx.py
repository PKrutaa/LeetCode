class Solution:
    def mySqrt(self, x: int) -> int:
        raiz = 1
        while raiz * raiz <= x:
            raiz += 1
        return raiz - 1