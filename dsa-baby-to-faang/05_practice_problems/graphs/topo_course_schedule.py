"""
Problem: Course Schedule (LeetCode #207)
Pattern: Topological Sort (Kahn's BFS)
Difficulty: Medium

Baby Explanation:
    You have courses numbered 0 to n-1 and some prerequisites. For example,
    to take course 1 you must first take course 0. We need to check if it's
    possible to finish all courses. If there's a circular dependency, it's impossible.

Example:
    Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    Output: True
    Explanation: Take 0, then 1 and 2, then 3. All courses can be completed.

Approach:
    1. Build an adjacency list and count indegrees (number of prerequisites).
    2. Add all courses with 0 prerequisites to a queue (they can be taken first).
    3. Process the queue: for each course, reduce indegree of its dependents.
    4. If a dependent's indegree becomes 0, add it to the queue.
    5. If we processed all courses, return True. Otherwise there's a cycle.

Time Complexity: O(V + E) - V is courses, E is prerequisites
Space Complexity: O(V + E) - adjacency list and indegree array
"""

from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Build adjacency list and indegree count
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)  # prereq -> course
            indegree[course] += 1

        # Step 2: Start with courses that have no prerequisites
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        # Step 3: Process courses in topological order
        courses_taken = 0
        while queue:
            course = queue.popleft()
            courses_taken += 1

            # Step 4: Reduce indegree for dependent courses
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Step 5: If all courses were taken, no cycle exists
        return courses_taken == numCourses


# --- Test Cases ---
if __name__ == "__main__":
    sol = Solution()

    # Test 1: Can finish all courses
    assert sol.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == True

    # Test 2: Cycle exists - impossible
    assert sol.canFinish(2, [[1, 0], [0, 1]]) == False

    # Test 3: No prerequisites at all
    assert sol.canFinish(3, []) == True

    # Test 4: Simple chain
    assert sol.canFinish(3, [[1, 0], [2, 1]]) == True

    # Test 5: Edge case - single course
    assert sol.canFinish(1, []) == True

    print("All tests passed!")
