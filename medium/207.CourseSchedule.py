# There are a total of numCourses courses you have to take, labeled
# from 0 to numCourses - 1. You are given an array prerequisites where
# prerequisites[i] = [ai, bi] indicates that you must take course bi
# first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = {}
        self.noncycle = True
        for start, end in prerequisites:
            if start not in self.graph.keys():
                self.graph[start] = []
            self.graph[start].append(end)
            if end not in self.graph.keys():
                self.graph[end] = []

        self.temp_marks = set()
        self.perm_marks = set()

        for n in self.graph:
            if self.noncycle:
                self.visit(n)
            else:
                return False


        return True

    def visit(self, m):
        if m in self.perm_marks:
            return
        if m in self.temp_marks:
            self.noncycle = False
            return
        self.temp_marks.add(m)

        for r in self.graph[m]:
            self.visit(r)
            if not self.noncycle:
                return
        self.temp_marks.remove(m)
        self.perm_marks.add(m)

