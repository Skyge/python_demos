# -*- coding:utf-8 -*-
# 2018/01/20
# version 1.0

'''
    Given a string s, 
    find the longest palindromic substring in s. 
    You may assume that the maximum length of s is 1000.
'''
    
class Solution():
    """
    Example:

        Input: "babad"

	Output: "bab"

	Note: "aba" is also a valid answer.

    Example:

	Input: "cbbd"

	Output: "bb"
    """
    def longest_palindrome(self, s):
        if len(s) < 2:
            return s
        max_len = 1
        start = 0
        for i in range(len(s)):
            if i-max_len >= 1 and s[i-max_len-1:i+1] == s[i-max_len-1:i+1][::-1]:
                start = i-max_len-1
                max_len += 2
                continue
            if i-max_len >= 0 and s[i-max_len:i+1] == s[i-max_len:i+1][::-1]:
                start = i-max_len
                max_len += 1
        return s[start:start+max_len]

        
        
if __name__ == "__main__":
    a = Solution()
    palindrome = a.longest_palindrome("caba")
    print(palindrome)
