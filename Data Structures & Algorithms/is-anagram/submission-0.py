class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap={}

        for character in s:
            if character not in hmap:
                hmap[character]=0
            hmap[character]+=1
        for character in t:
            if character not in hmap:
                hmap[character]=0
            hmap[character]-=1
        for value in hmap:
            if hmap[value]!= 0:
                return False
        return True