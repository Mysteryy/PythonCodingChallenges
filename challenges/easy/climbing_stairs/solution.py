class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        # The number of ways to get to n is the sum of the number of ways to get to n-1, and n-2
        # This is because we can get to n by taking 1 step (from n-1) or 2 steps (from n-2)
        first_sum = 1
        second_sum = 2
        for i in range(3, n):
            first_sum, second_sum = second_sum, first_sum + second_sum

        return first_sum + second_sum
