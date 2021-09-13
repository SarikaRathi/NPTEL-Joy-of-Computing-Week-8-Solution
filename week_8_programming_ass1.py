# Week 8 Programming Assignment 1

# Given a string as input, determine if it is a palindrome or not. (Ignore the spaces, case and any punctuation or special characters present in the string). 

# Note: A palindromes is a string which has characters in the same order when read forward or backwards.
NO_OF_CHARS = 256
def canFormPalindrome(str1):
    # Get lengths of both strings
   
    
    count = [0] * (NO_OF_CHARS)
  
    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in range(0, len(str1)):
        count[ord(str1[i])] = count[ord(str1[i])] + 1
  
    # Count odd occurring characters
    odd = 0
  
    for i in range(0, NO_OF_CHARS):
        if (count[i] & 1):
            odd = odd + 1
  
        if (odd > 1):
            return False
  
    # Return true if odd count is 0 or 1,
    return True
        
# Driver code
st1 = input()

str1=''.join(filter(str.isalnum, st1.casefold()))

# Function Call
if canFormPalindrome(str1):
    print("Yes",end="")
else:
    print("No",end="")