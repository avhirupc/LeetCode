"""Recursive"""
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		def lcsUtil(text1: str,text2: str):
			if text1=="" or text2=="":
				return 0
			if text1[-1]==text2[-1]:
				return 1 + lcsUtil(text1[:-1],text2[:-1])
			return max(lcsUtil(text1,text2[:-1]),lcsUtil(text1[:-1],text2))
		lcs_len = lcsUtil(text1,text2)
		return lcs_len

"""Memoization version 1"""
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		memory={}
		def lcsUtil(text1: str,text2: str):
			nonlocal memory
			if (text1,text2) in memory:
				return memory[(text1,text2)]
			if text1=="" or text2=="":
				memory[(text1,text2)] = 0
				return 0
			if text1[-1]==text2[-1]:
				res = 1 + lcsUtil(text1[:-1],text2[:-1])
				memory[(text1,text2)]= res
				return res
			res = max(lcsUtil(text1,text2[:-1]),lcsUtil(text1[:-1],text2))
			memory[(text1,text2)] = res
			return res
		lcs_len = lcsUtil(text1,text2)
		return lcs_len

"""Memoization version 2"""
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		memory=[[-1 for c in range(len(text2)+1)]for r in range(len(text1)+1)]
		def lcsUtil(text1: str,text2: str):
			nonlocal memory
			r,c =len(text1),len(text2)
			if memory[r][c]!=-1:
				return memory[r][c]
			if text1=="" or text2=="":
				res = 0
			elif text1[-1]==text2[-1]:
				res = 1 + lcsUtil(text1[:-1],text2[:-1])
			else:
				res = max(lcsUtil(text1,text2[:-1]),lcsUtil(text1[:-1],text2))
			memory[r][c] = res 
			return memory[r][c]

		
		lcs_len = lcsUtil(text1,text2)
		return lcs_len

"""Bottom Up Version"""
class Solution:
	def longestCommonSubsequence(self, text1: str, text2: str) -> int:
		def lcsUtil(text1: str,text2: str):
			memory=[[-1 for c in range(len(text2)+1)]for r in range(len(text1)+1)]
			rows,columns =len(text1)+1,len(text2)+1
			for r in range(rows):
				memory[r][0]=0
			for c in range(columns):
				memory[0][c]=0
			for r in range(1,rows):
				for c in range(1,columns):
					if r==0 or c==0:
						memory[r][c]=0
						continue
					if text1[r-1]==text2[c-1]:
						memory[r][c]=1+memory[r-1][c-1]
					else:
						memory[r][c]= max(memory[r][c-1],memory[r-1][c])

			return memory[r][c]

		
		lcs_len = lcsUtil(text1,text2)
		return lcs_len


