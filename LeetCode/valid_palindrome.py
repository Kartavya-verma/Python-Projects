# Method - 1
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         import re
#         s = re.sub('[^0-9a-zA-Z]+', '', s)
#         s = s.lower()
#         return s == s[::-1]


# Method - 2
s = "A man, a plan, a canal: Panama"
s = "".join(x for x in s if x.isalnum()).lower()
# return s == s[::-1]
print(s)
print(s[::-1])