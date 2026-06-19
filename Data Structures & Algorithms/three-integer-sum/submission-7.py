from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums)):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate second numbers
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate third numbers
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif s < 0:
                    j += 1

                else:
                    k -= 1

        return result