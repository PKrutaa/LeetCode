class Solution:
    def solve(self, n):
        if n == 0 or n == 1:
            return n
        return self.solve(n - 1) + self.solve(n - 2)
        
    def fib(self, n: int) -> int:
        return self.solve(n)
