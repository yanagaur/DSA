class Solution:
    def count_digits(self, x):
        count = 0
        while x > 0:
            count += 1
            x //= 10
        return count
    
    def digitsInFactorial(self, N):
        fact = 1
        for i in range(1, N + 1):
            fact *= i
        return self.count_digits(fact)
