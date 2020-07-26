class Solution:
	def minInsertions(self, s: str) -> int:
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
		return len(s) - lcsUtil(s,s[::-1]) 