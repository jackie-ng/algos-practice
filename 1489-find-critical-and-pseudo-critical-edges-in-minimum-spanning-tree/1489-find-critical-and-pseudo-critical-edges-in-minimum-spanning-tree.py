class Solution:

    class UnionFind:
        def __init__(self, n):
            self.root = list(range(n))
            self.rank = [1] * n
            self.max_size = 1

        def find(self, x):
            # Finds the root of x
            if x != self.root[x]:
                self.root[x] = self.find(self.root[x])
            return self.root[x]

        def union(self, x, y):
            # Connects x and y
            root_x = self.find(x)
            root_y = self.find(y)
            if root_x != root_y:
                if self.rank[root_x] < self.rank[root_y]:
                    root_x, root_y = root_y, root_x
                self.root[root_y] = root_x
                self.rank[root_x] += self.rank[root_y]
                self.max_size = max(self.max_size, self.rank[root_x])
                return True
            return False

    def findCriticalAndPseudoCriticalEdges(self, n, edges):
        new_edges = [edge.copy() for edge in edges]
        # Add index to edges for tracking
        for i, edge in enumerate(new_edges):
            edge.append(i)
        # Sort edges based on weight
        new_edges.sort(key=lambda x: x[2])

        # Find MST weight using union-find
        uf_mst = self.UnionFind(n)
        mst_weight = 0
        for u, v, w, _ in new_edges:
            if uf_mst.union(u, v):
                mst_weight += w

        # Check each edge for critical and pseudo-critical
        critical = []
        pseudo_critical = []
        for (u, v, w, i) in new_edges:
            # Ignore this edge and calculate MST weight
            uf_ignore = self.UnionFind(n)
            ignore_weight = 0
            for (x, y, w_ignore, j) in new_edges:
                if i != j and uf_ignore.union(x, y):
                    ignore_weight += w_ignore
            # If the graph is disconnected or the total weight is greater,
            # the edge is critical
            if uf_ignore.max_size < n or ignore_weight > mst_weight:
                critical.append(i)
                continue

            # Force this edge and calculate MST weight
            uf_force = self.UnionFind(n)
            force_weight = w
            uf_force.union(u, v)
            for (x, y, w_force, j) in new_edges:
                if i != j and uf_force.union(x, y):
                    force_weight += w_force
            # If total weight is the same, the edge is pseudo-critical
            if force_weight == mst_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]