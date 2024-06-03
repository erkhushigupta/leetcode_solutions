class Solution:
    def numOfWays(self, nums: List[int]) -> int:
 

        # Define a recursive function to calculate the number of BSTs for the given list.

        def count_bsts(sub_nums):

            # Base case: if the list is empty or has only one element, there is only one way to construct a BST.

            if len(sub_nums) < 2:

                return 1

          

            # Split the nums based on the current root, which is the first element in the list.

            left_subtree = [x for x in sub_nums if x < sub_nums[0]]

            right_subtree = [x for x in sub_nums if x > sub_nums[0]]

          

            # Calculate the possibilities of left and right subtrees.

            left_ways = count_bsts(left_subtree)

            right_ways = count_bsts(right_subtree)

          

            # Calculate the combination count using precomputed combination values.

            left_size = len(left_subtree)

            right_size = len(right_subtree)

          

            # Calculate the result as the product of left ways, right ways, and the combination count.

            # Mod operations are used to keep the values within integer limits specified by the problem.

            return ((comb[left_size + right_size][left_size] * left_ways) % MOD) * right_ways % MOD


        # Length of the input list of numbers.

        n = len(nums)

        # The modulo value given by the problem to perform operations under this modular arithmetic.

        MOD = 10 ** 9 + 7

      

        # Initialize combination values for future use in the recursive function to calculate combos (binomial coefficients).

        comb = [[0] * n for _ in range(n)]

        # The first column of Pascal's Triangle (nC0) is 1.

        for i in range(n):

            comb[i][0] = 1

      

        # Populate Pascal's Triangle to find combinations (nCr) under modulo MOD.

        for i in range(1, n):

            for j in range(1, i + 1):

                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD

      

        # The final count needs to subtract 1 to not count the initial empty BST.

        # Then, we also ensure the result is in the correct modulo range by adding MOD and again applying mod.

        return (count_bsts(nums) - 1 + MOD) % MOD
