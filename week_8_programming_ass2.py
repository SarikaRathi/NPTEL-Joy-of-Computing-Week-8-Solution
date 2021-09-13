# NPTEL Week 8 Programming Assignment 2
# Given two strings as input, determine if they are anagrams or not. (Ignore the spaces, case and any punctuation or special characters). 

# Note: Anagrams are the strings which are made up of the same set of letters. For example : Mary and Army are anagrams.


def areAnagram(str1, str2):
    # Get lengths of both strings
    n1 = len(str1)
    n2 = len(str2)
 
    # If lenght of both strings is not same, then
    # they cannot be anagram
    if n1 != n2:
        return 0
 
    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)
 
    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 0
 
    return 1
 
 
# Driver code
st1 = input()
st2 = input()
str1=''.join(filter(str.isalnum, st1.casefold()))
str2=''.join(filter(str.isalnum, st2.casefold()))

# Function Call
if areAnagram(str1, str2):
    print("Yes",end="")
else:
    print("No",end="")
