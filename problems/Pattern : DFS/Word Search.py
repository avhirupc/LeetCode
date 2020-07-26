"""Accepted"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not word:
            return False
        rows, columns = len(board), len(board[0])
        for row_itr in range(rows):
            for col_itr in range(columns):
                traversed_points = set([])
                if self.dfs(word, row_itr, col_itr, board, traversed_points):
                    return True
        return False

    def dfs(self, word, row_itr, col_itr, board, traversed):
        # condition for already traversed remaining
        if row_itr < 0 or row_itr >= len(board) or col_itr < 0 or col_itr >= len(board[0]):
            return False
        if (row_itr, col_itr) in traversed:
            return False
        if board[row_itr][col_itr] != word[0]:
            return False
        if board[row_itr][col_itr] == word[0] and len(word) == 1:
            return True
        if self.dfs(
            word[1:], row_itr, col_itr - 1, board, traversed.union([(row_itr, col_itr)])
        ):
            return True

        if self.dfs(
            word[1:], row_itr, col_itr + 1, board, traversed.union([(row_itr, col_itr)])
        ):
            return True
        if self.dfs(
            word[1:], row_itr - 1, col_itr, board, traversed.union([(row_itr, col_itr)])
        ):
            return True
        if self.dfs(
            word[1:], row_itr + 1, col_itr, board, traversed.union([(row_itr, col_itr)])
        ):
            return True
        return False
