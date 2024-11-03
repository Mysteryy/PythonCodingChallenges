class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return s and goal and len(s) == len(goal) and (s + s).find(goal) != -1
