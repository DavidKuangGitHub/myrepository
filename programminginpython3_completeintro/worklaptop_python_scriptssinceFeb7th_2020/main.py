"""
main.py
=================================================================================
The core module of my Sphinx project with leetcode_pythonq_58_LengthOfLastWord.py
"""

def about_me(your_name):
    """
    Return the most important thing about a person.

    Parameters
    ----------
    your_name
        A string indicating the name of the person.

    """
    return "The wise {} loves Python both v2&3.".format(your_name)


class sphinxSolution:
    """An example docstring for a class definition."""
    def lengthOfLastWord1(self, s: str) -> int:
        """
        Return result by calling lengthOfLastWord1
        """
        lst=s.strip().split()
        if lst!=[]:
            return len(lst[-1])
        return 0
        
    def lengthOfLastWord2(self, s: str) -> int:
        """
        Return result by calling lengthOfLastWord2
        """
        s=s.strip()
        if s=="":
            return 0
        if " " not in s:
            return len(s)
        ind=s.rfind(" ")
        return len(s[ind+1:])

    def about_self(self):
        """
        Return information about an instance created from the requirement.
        
        Given a string s consist of upper/lower-case alphabets and empty space character ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.
        
        If the last word does not exist, return 0.
        
        Note: A word is defined as a maximal substring consisting of non-space characters only.
        
        Example:
        Input: "Hello World"
        Output: 5
        
        """
        return "I am a very smart {} object.".format(self.name)
        
"""mysphinxSolution = sphinxSolution()
myString = "Hello World"
print("Result_lengthOfLastWord1 = ", mysphinxSolution.lengthOfLastWord1(myString)," !")
print("Result_lengthOfLastWord2 = ", mysphinxSolution.lengthOfLastWord2(myString)," as well !")"""
