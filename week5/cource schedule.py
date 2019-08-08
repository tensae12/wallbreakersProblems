class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = {}
        for course, preq in prerequisites:
            if course not in edges:
                edges[course] = [preq]
            else:
                edges[course].append(preq)

        def helper(path,course):
            for preq in edges[course]:
                if preq in path:
                    return False
                if preq in edges and preq not in preq_l:
                    path.add(preq)
                    check = helper(path,preq)
                    path.remove(preq)
                    if not check:
                        return False
                    else:
                        preq_l.add(preq)
            return True
        preq_l = set()
        for course in edges.keys():
            if not helper(set(),course):
                return False
        return True








        