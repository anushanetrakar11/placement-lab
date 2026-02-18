class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, node, start, end):
        if start == end:
            self.tree[node] = nums[start]
            return

        mid = (start + end) // 2
        self.build(nums, 2*node+1, start, mid)
        self.build(nums, 2*node+2, mid+1, end)

        self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def update(self, idx, val, node, start, end):
        if start == end:
            self.tree[node] = val
            return

        mid = (start + end) // 2
        if idx <= mid:
            self.update(idx, val, 2*node+1, start, mid)
        else:
            self.update(idx, val, 2*node+2, mid+1, end)

        self.tree[node] = max(self.tree[2*node+1], self.tree[2*node+2])

    def queryMax(self, L, R, node, start, end):
        if R < start or end < L:
            return float('-inf')

        if L <= start and end <= R:
            return self.tree[node]

        mid = (start + end) // 2
        left = self.queryMax(L, R, 2*node+1, start, mid)
        right = self
