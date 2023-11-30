#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
from unittest import result


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            O(n)，空间复杂度较高
        '''
        # result = []
        # temp = 0
        # for index, value in enumerate(nums):
        #     if target-value in nums[:index]+nums[index+1:]:
        #         result.append(index)
        #         temp += 1
        #     if temp == 2:
        #         break
        # return result

        '''
            O(n)，空间复杂度较高
        '''
        # temp = {}
        # result = []
        # for index, value in enumerate(nums):
        #     if target-value in temp:
        #         result = [temp[target - value], index]
        #         break
        #     temp[value] = index
        # return result
        '''
            O(n)
        '''
        # temp = {}
        # for index, value in enumerate(nums):
        #     if target-value in temp:
        #         return [temp[target - value], index]
        #     temp[value] = index
        '''
            O(logn)尝试
        '''
        # 构建带有索引的元组列表
        nums_with_index = [(num, index) for index, num in enumerate(nums)]

        # 对元组列表按照元素值排序
        nums_with_index.sort(key=lambda x: x[0])

        # 使用双指针查找
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return None  # 如果没有找到符合条件的两个数，返回None


# @lc code=end
