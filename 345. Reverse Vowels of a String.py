'''
First define aeiou as vowel so that it can be search through
delcare string as a list of s
loop through the list one by one in the list
if a character in the list is not a vowel move foward(a), backward(b)
if they are vowel then switch their position around
until the loop to a<b join the list into a string and return the string 
'''
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        #define vowel
        
        vowel = "aeiou"
        string = list(s)
        a,b = 0, len(s) - 1
        while a < b:
            if string[a].lower() not in vowel:
                a += 1
            elif string[b].lower() not in vowel:
                b -=1
            else:
                string[a],string[b] = string[b], string[a]
                a += 1
                b -= 1
        return "".join(string) 