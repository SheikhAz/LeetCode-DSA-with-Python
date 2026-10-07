class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1,n + 1)]
        result = []
        factorial = math.factorial(n)
        index =  k - 1
        while nums:
            factorial = factorial // len(nums)
            pos = index // factorial
            number = nums.pop(pos)
            result.append(number)
            index = index % factorial
        return "".join(result)