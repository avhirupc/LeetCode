class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        solutions = {}
        prefix = []
        candidates = sorted(candidates)
        for pos in range(len(candidates)):
            if pos!=0 and candidates[pos]==candidates[pos-1]:
                continue
            self.combinationSum2Util(
                pos,
                candidates,
                target - candidates[pos],
                prefix + [candidates[pos]],
                solutions,
            )

        return list(solutions.values())

    def combinationSum2Util(self, pos, candidates, target, prefix, solutions):
        if 0 > target:
            return
        if 0 == target:
            solutions[tuple(prefix)]=prefix
            return
        for next_pos in range(pos + 1, len(candidates)):
            self.combinationSum2Util(
                next_pos,
                candidates,
                target - candidates[next_pos],
                prefix+[candidates[next_pos]],
                solutions
            )
        return
