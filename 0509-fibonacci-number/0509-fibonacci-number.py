class Solution:
    def fib(self, N):
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

 
