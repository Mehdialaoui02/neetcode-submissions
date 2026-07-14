class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t) :
			return False

		n = len(s)
		counterS = [0] * 26
		counterT = [0] * 26

		for i in range(len(s)) :
			counterS[ord(s[i]) - ord('a')] += 1
			counterT[ord(t[i]) - ord('a')] += 1

		return counterS == counterT
