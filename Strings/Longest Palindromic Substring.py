class Solution:
    def longestPalindrome(self, s):
        max_length = 1
        palin_length = {}
        right_temp_palin = 0
        left_temp_palin = 0
        length = 1
        center = 0

        for i in range(len(s)):
            palin_left = i-1
            palin_right = i+1
            mirror_palin_index = 2 * center - i
            mirror_palin_length = None
            side_mirror_palin_length = None
            if mirror_palin_index in palin_length.keys():
                mirror_palin_length = palin_length[mirror_palin_index]
                side_mirror_palin_length = mirror_palin_length // 2
            if side_mirror_palin_length != None and len(s) > mirror_palin_index >= 0 and i + side_mirror_palin_length < right_temp_palin and i - side_mirror_palin_length >left_temp_palin:
                palin_length[i] = mirror_palin_length
                continue
            while palin_left >=0 and palin_right<len(s):
                if s[palin_left] == s[palin_right]:
                    length += 2
                    palin_right += 1
                    palin_left -= 1
                else:
                    break
            if max_length < length:
                max_length = length
                center = i
                right_temp_palin = center + (length // 2)
                left_temp_palin = center - (length // 2)

            palin_length[i] = length
            length = 1


        return s[left_temp_palin:right_temp_palin+1]



s = "tracecarmalayalambace"
print(str(Solution().longestPalindrome(s)))
# racecar
