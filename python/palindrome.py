import re
    
def palindrome(word):
    
    word = str(word).lower()
    word = re.sub(r"\W", "", word)
    # .isalnum()  can also determine if currentElem is alphanumeric and return True or False
    # print(word)
    
    if word == word[::-1]:
        return True

    return False


# print(palindrome('racecar'))
# print(palindrome('Noon'))
# print(palindrome('ciVic'))
# print(palindrome('nice'))
# # print(palindrome(434))
# # print(palindrome(123))
# print(palindrome('bomb'))

# print("The following should be True if you're trying to do the extra portion of this challenge")
# print(palindrome('Sore was I ere I saw Eros.'))
# print(palindrome('A man, a plan, a canal -- Panama'))
