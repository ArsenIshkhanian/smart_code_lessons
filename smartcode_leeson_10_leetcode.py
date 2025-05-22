# Exercise 1
# class Solution:
#     def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if n > 0: 
#             nums1[m:] = nums2
#             nums1.sort()
# list1 = [4, 0, 0, 0, 0, 0]
# m = 1
# list2 = [2, 4, 5, 3, 7]
# n = 5
# solver = Solution(list1, m, list2, n)
# solver.merge(list1, m, list2, n)


# Exercise 2
# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         nums[::] = [num for num in nums if num != val]
#         return len(nums)
# list1 = [1, 0, 3, 2, 4, 4, 3, 3]
# val = 3
# k = Solution().removeElement(list1, val)
# print(k)


# Exercise 3
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         nums[::] = list(set(nums))
#         nums.sort()
#         return len(nums)
# nums = [0,0,1,1,1,2,2,3,3,4]
# solver = Solution().removeDuplicates(nums)


# Exercise 4
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         min_value = min(nums)
#         max_value = max(nums)
#         nums[::] = [num for num in range(min_value, max_value + 1) for _ in range(min(2, nums.count(num)))]
#         print(nums)
#         return(len(nums))    
# list1 = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4]
# solver = Solution().removeDuplicates(list1)


# Exercise 5
# class Solution:
#     def majorityElement(self, nums:list[int]) -> int:
#         from collections import Counter
#         data = Counter(nums)
#         for key in data:
#             if data[key] > len(nums) // 2:
#                 print(data[key])
# nums = [2,2,1,1,1,2,2]
# solver = Solution().majorityElement(nums)


# Exercise 6
# class Solution:
#     def rotate(self, nums: list[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         variable = k % len(nums)
#         part = nums[-variable:]
#         del nums[-variable:]
#         nums[::] = list(part) + nums[::]
#         print(nums)
#         return
# list1 = [1, 2, 3, 4, 5]
# k = 2
# solver = Solution().rotate(list1, k)


# Exercise 7
# class Solution:
#     def isSubSequence(self, sequence:str, text:str):
#         i = 0
#         j = 0
#         while True:
#             if i == len(sequence):
#                 return True
#             if j == len(text):
#                 return False
#             if sequence[i] == text[j]:
#                 i += 1
#                 j += 1
#             else:
#                 j += 1
# sequence = 'aec'
# text = 'ahelcr'
# solver = Solution().isSubSequence(sequence, text)
# print(solver)


# Exercise 8
# class Solution:
#     def climbStairs(self, n: int) -> int:
        # solution 1
        # if n == 0:
        #     return 1
        # elif n < 0:
        #     return 0
        # else:
        #     return Solution().climbStairs(n - 1) + Solution().climbStairs(n - 2)
        # solution 2
        # remainder = n % 2
        # min_step = n // 2
        # count = 0
        # twos_inside_step = 0
        # for step in range(n, min_step, -1):
        #     numerator = 1
        #     for i in range(step, step - twos_inside_step, -1):
        #         numerator *= i
        #     denominator = 1
        #     for j in range(twos_inside_step, 0, -1):
        #         denominator *= j
        #     value = numerator / denominator
        #     count += value
        #     twos_inside_step += 1
        # if not remainder:
        #     count += 1
        # return int(count)

        # solution 3
        # if n <= 3: return n
        # count = 0
        # prev2 = 3
        # prev1 = 2
        # for _ in range(3, n):
        #     count = prev2 + prev1
        #     prev1 = prev2
        #     prev2 = count
        # return count
# n = 2
# solver = Solution().climbStairs(n)
# print(solver)


# Exercise 9
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         x = str(x)
#         return x== x[::-1]
# x = 1221
# solver = Solution().isPalindrome(x)


# Exercise 10
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman = {
#             'I':1,
#             'V':5,
#             'X':10,
#             'L':50,
#             'C':100,
#             'D':500,
#             'M':1000
#         }
#         number = 0
#         for i in range(0, len(s)):
#             if i == len(s) - 1:
#                 number += roman[s[i]]
#             elif roman[s[i]] < roman[s[i + 1]]:
#                 number -= roman[s[i]]
#             else:
#                 number += roman[s[i]]
#         return number
# s = 'MCMXCIV'
# solver = Solution().romanToInt(s)


# Exercise 11
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         words = s.strip().split(' ')
#         length = len(words[-1])
#         print(length)
# s = 'Hello World'
# solver = Solution().lengthOfLastWord(s)


# Exercise 12
# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         i = -1
#         prefix = ''
#         max_loop = len(min(strs, key=len))
#         while True:
#             for loop in range(max_loop):
#                 i += 1
#                 example = strs[0][i]
#                 for word in strs[1:]:
#                     if word[i] == example:
#                         continue
#                     else:
#                         return prefix
#                 prefix += example
#                 print(prefix)
#             return prefix
# strs = ["flower","flow","flight"]
# solver = Solution().longestCommonPrefix(strs)
# print(solver)


# Exercise 13
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         best_price = prices[0]
#         max_profit = 0
#         for price in prices[1:]:
#             if best_price > price:
#                 best_price = price
#             elif max_profit < price - best_price:
#                 max_profit = price - best_price
#         return max_profit
# prices = [2,1,2,1,0,1,2]
# solver = Solution().maxProfit(prices)
# print(solver)

# Exercise 14
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         import re
#         cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)
#         return cleaned_text.lower() == cleaned_text[::-1].lower()
# s = 'A man, a plan, a canal: Panama'
# solver = Solution().isPalindrome(s)
# print(solver)


# Exercise 15
# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         for letter in ransomNote:
#             if letter in magazine:
#                 magazine = magazine.replace(letter, '', 1)
#                 print(magazine)
#             else:
#                 return False
#         return True
# r = 'aa'
# m = 'ab'
# solver = Solution().canConstruct(r, m)
# print(solver)



# Exercise 16
# class Solution:
#     def canJump(self, nums: list[int]) -> bool:
#         list_of_list = []
#         def recursion(nums, list_of_list):
#             print(list_of_list)
#             if nums == []:
#                 return False
#             elif len(nums) == 1:
#                 return True
#             elif nums in list_of_list:
#                 return False
#             else:
#                 list_of_list.append(nums)
#                 value = nums[0]
#                 for i in range(value, 0, -1):
#                     half_result = recursion(nums[i:], list_of_list)
#                     if half_result == True:
#                         return half_result
#                     else:
#                         continue
#                 return False
#         result = recursion(nums, list_of_list)
#         return result
# nums = [3, 2, 1, 1, 0, 4]
# solver = Solution().canJump(nums)
# print(solver)



# Exercise 17
# class Solution:
#     def plusOne(self, digits: list[int]) -> list[int]:
#         i = len(digits) - 1
#         while digits[i] == 9:
#             digits[i] = 0
#             if i == 0:
#                 return [1] + digits
#             i -= 1
#         else:
#             digits[i] += 1
#             return digits
# integers = [1, 2, 3, 9, 9]
# solver = Solution().plusOne(integers)
# print(solver)



# Exercise 18
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 2:
#             return x
#         left = 1
#         right = x
#         while left <= right:
#                 middle = (left + right) // 2
#                 if middle * middle == x:
#                      return middle
#                 elif middle * middle > x:
#                      right = middle - 1
#                 else:
#                      left = middle + 1
#         return right      
# numb = 4
# solver = Solution().mySqrt(numb)
# print(solver)



# Exercise 19
# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         dict_for_letters = dict()
#         for i in range(len(s)):
#             print(dict_for_letters)
#             if s[i] in dict_for_letters.keys():
#                 if dict_for_letters[s[i]] != t[i]:
#                     return False
#             elif t[i] in dict_for_letters.values():
#                 return False
#             dict_for_letters[s[i]] = t[i]
#         print(dict_for_letters)
#         return True
# s = 'paper'
# t = 'title'
# solver = Solution().isIsomorphic(s, t)
# print(solver)



# Exercise 20
# class Solution:
#     def wordPattern(self, pattern: str, s: str) -> bool:
#         dict_for_letters = dict()
#         s = s.split()
#         if len(s) != len(pattern):
#             return False
#         for i in range(len(s)):
#             if s[i] in dict_for_letters.keys():
#                 if dict_for_letters[s[i]] != pattern[i]:
#                     return False
#             elif pattern[i] in dict_for_letters.values():
#                 return False
#             dict_for_letters[s[i]] = pattern[i]
#         return True
# pattern = "abba"
# s = "dog cat cat fish"
# solver = Solution().wordPattern(pattern, s)
# print(solver)



# Exercise 21
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         from collections import Counter
#         return Counter(s) == Counter(t)
# s = "anagram"
# t = "nagaram"
# solver = Solution().isAnagram(s, t)
# print(solver)



# Exercise 22
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for index, n in enumerate(nums):
#             nums[index] = None
#             if target - n in nums:
#                 return[index, nums.index(target - n)]
# nums = [0, 4, 3, 0]
# target = 0
# solver = Solution().twoSum(nums, target)
# print(solver)



# Exercise 23
# class Solution:
#     def isValid(self, s: str) -> bool:
#         mylist = []
#         dict_ = {
#             '}': '{',
#             ')': '(',
#             ']': '[',
#         }
#         for i in s:
#             if i in dict_.values():
#                 mylist.append(i)
#             elif mylist and dict_[i] != mylist[-1]:
#                 return False
#             elif not mylist and i in dict_.keys():
#                 return False
#             elif mylist:
#                 mylist.pop()
#         print(mylist)
#         return not mylist
# s = "]"
# solver = Solution().isValid(s)
# print(solver)


# Exercise 24
# class Solution:
#     def singleNumber(self, nums: list[int]) -> int:
#         result = 0
#         for i in nums:
#             result ^= i
#         return result
# array = [4, 1, 2, 2 ,1, 4, 5, 5, 3, 2, 2]
# solver = Solution().singleNumber(array)
# print(solver)



# Exercise 25
# import math
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         sum = 0
#         while n != 0:
#             devider = n // 2
#             sum += n - devider * 2
#             n = n // 2
#         print(sum)
# number = 17
# solver = Solution().hammingWeight(number)
# print(solver)



# Exercise 26
# class Solution:
#     def searchInsert(self, nums: list[int], target: int) -> int:
#         start = 0
#         end = len(nums) - 1
#         while start <= end:
#                 middle = (start + end) // 2
#                 if nums[middle] > target:
#                        end = middle - 1
#                 elif nums[middle] < target:
#                        start = middle + 1
#                 else:
#                        return middle
#         return start
# nums = [1, 3, 5, 6]
# target = 5
# solver = Solution().searchInsert(nums, target)
# print(solver)



# Exercise 27
# class Solution:
#     def summaryRanges(self, nums: list[int]) -> list[str]:
#         if len(nums) == 1:
#             return [nums[0]]
#         result = []
#         k = 0
#         condition = True
#         for i in range(len(nums)):
#             print(result)
#             if i == len(nums) - 1 and nums[i] == nums[i - 1] + 1:
#                 result[-1] += f"{k}"
#                 break
#             elif i == len(nums) - 1 and nums[i] != nums[i - 1] + 1:
#                 result.append(f"{nums[i]}")
#                 break
#             if i == 0 and nums[i] != nums[i + 1] - 1:
#                 result.append(f"{nums[i]}")
#             elif i > 0 and nums[i] != nums[i - 1] + 1 and nums[i] != nums[i + 1] - 1:
#                 result.append(f"{nums[i]}")
#             elif nums[i] == nums[i + 1] - 1:
#                 if condition:
#                     result.append(f"{nums[i]}->")
#                     condition = False
#                 k = nums[i + 1]
#             else:
#                 result[-1] += f"{k}"
#                 condition = True
#         return result
# nums = [0,2,3,4,6,8,9]
# solver = Solution().summaryRanges(nums)
# print(solver)



# Exercise 28
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         sum = n
#         used_list = []
#         while sum != 1:
#             used_list.append(sum)
#             sum = 0
#             for i in str(n):
#                 sum += int(i) ** 2
#             if sum in used_list:
#                 return False
#             n = sum
#         return True
# n = 7
# solver = Solution().isHappy(n)
# print(solver)


# Exercise 29
# class Solution:
#     def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # solution 1
        # used = {}
        # for i, num in enumerate(nums):
        #     if i in used and i - used[i] <= k:
        #         return True
        #     used[num] = i
        # return False
        # solution 1
        # if len(nums) == len(set(nums)): return False
        # solution 2
        # left = 1
        # right = left + k
        # for i in range(len(nums)):
        #     if nums[i] in nums[left:right]:return True
        #     left += 1
        #     if right < len(nums): roght += 1
        # return False
# nums = [1, 2, 3, 4, 6, 2, 1]
# k = 3
# solver = Solution().containsNearbyDuplicate(nums, k)
# print(solver)


# Exercise 30
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         profit = 0
#         for i in range(len(prices) - 1):
#             min_price = prices[i]
#             best_price = prices[i + 1]
#             if best_price > min_price:
#                 profit += best_price - min_price
            
#         return profit

# prices = [7,1,5,3,6,4]
# solver = Solution().maxProfit(prices)
# print(solver)


# Exercise 31
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(i for i in s.strip().split()[::-1] if i != ' ')
    

# solver = Solution().reverseWords('a good   example')
# print(solver)


# Exercise 32
# class Solution:
#     def twoSum(self, numbers: list[int], target: int) -> list[int]:
#         l = 0
#         r = len(numbers) - 1
#         while l < r:
#             if numbers[l] + numbers[r] > target:
#                 r -= 1
#             elif numbers[l] + numbers[r] < target:
#                 l += 1
#             else:
#                 return [l + 1, r + 1]
#         return []
            
    

# numbers = [2,3,4]
# target = 6
# solver = Solution().twoSum(numbers, target)
# print(solver)


# Exercise 33
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         areas = []
#         for i in range(len(height)):
#             for j in range(i + 1, len(height)):
#                 height_ = min(height[i], height[j])
#                 distance = j - i
#                 areas.append(height_ * distance)
#         print(max(areas))


# height = [1,8,6,2,5,4,8,3,7]
# solver = Solution().maxArea(height)
# print(solver)



# Exercise 34
# def maxim(nums, amount, count = []):
#     if nums == []:
#         amount.append(sum(count))
#     for i in range(min(2, len(nums))):
#         count.append(nums[i])
#         maxim(nums[i + 2:], amount, count)
#         count.pop()
#     return max(amount)
        

            
# nums = [4, 1, 2, 7, 5, 3, 1]
# amount = []
# result = maxim(nums, amount)
# print(result)


# Exercise 35
# class Solution:
#     def trailingZeroes(self, n: int) -> int:
#         if n < 5:
#             return 0
#         else:
#             sum = 0
#             while n >= 5:
#                 sum += n // 5
#                 n //= 5
#             return sum

# n = 50
# solver = Solution().trailingZeroes(n)
# print(solver)



# Exercise 36
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         def helper(x, n):
#             if x == 0: return 0
#             if n == 0: return 1

#             result = helper(x * x, n // 2)
#             return x * result if n % 2 == 1 else result
            
#         result = helper(x, abs(n))
#         return result if n > 0 else 1 / result

# solver = Solution().myPow(5, 4)
# print(solver)


# Exercise 37
# class Solution:
#     def longestConsecutive(self, nums: list[int]) -> int:
#         count = []
#         i = 0
#         length = []
#         while i < len(nums):
#             if (nums[i] - 1 in nums or nums[i] + 1 in nums) and nums[i] not in length:
#                 print(nums[i])
#                 length.append(nums[i])
#             else:
#                 count.append(len(length))
#                 length = []
#             i += 1
#         return max(count)


# nums = [100,4,200,1,3,2]
# solver = Solution().longestConsecutive(nums)
# print(solver)






