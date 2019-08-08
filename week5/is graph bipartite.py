class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0] * len(graph)
        for node in range(len(graph)):
            if not visited[node]:
                stack = [node]
                visited[node] = 1
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if visited[neighbor] == visited[node]:
                            return False
                        if not visited[neighbor]:
                            stack.append(neighbor)
                            visited[neighbor] = visited[node] * (-1)
        return True