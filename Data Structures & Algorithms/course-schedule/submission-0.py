class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = set()

        def dfs(crs):
            if preMap[crs] == []:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True