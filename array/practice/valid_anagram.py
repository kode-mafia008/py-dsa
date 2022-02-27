# Given two strings s and t, return true if anagram else false


from typing import Counter


class Anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t) #second solution Counter is a function by python
        # return sorted(s) == sorted(t) #third  solution
        
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countS[t[i]] = 1 + countS.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
