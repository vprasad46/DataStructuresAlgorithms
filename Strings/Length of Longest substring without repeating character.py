class Solution:
    def lengthOfLongestSubstring(self, s):
        word_dict = {}
        max_length = 0
        temp_length = 0
        for char in s:
            if not char in word_dict :
                word_dict[char] = 1
                temp_length += 1
            else:
                if temp_length > max_length:
                    max_length = temp_length
                temp_length = 0
                word_dict = {}
        return max_length

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10
