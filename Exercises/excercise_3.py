# -*- coding:utf-8 -*-
#2018/01/08
#version 1.0

'''
    Given a string,
    find the length of the longest substring without repeating characters.
'''

def length_of_longest_substring(s):
    """
        Examples:

        Given "abcabcbb", the answer is "abc", which the length is 3.

        Given "bbbbb", the answer is "b", with the length of 1.
        
    """
    substring = {}
    max_length = start = 0
    
    for i in range(len(s)):
        if s[i] in substring:
            start = substring[s[i]] + 1
        else:
            max_length = max(max_length, i-start+1)
            
        substring[s[i]] = i
            
    return max_length
        
    

if __name__ == "__main__":
    s = "pwwkew"
    print(length_of_longest_substring(s))


        
            
        
        
            
