class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        inorder_idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left: int, right: int) -> TreeNode | None:
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_idx_map[root_val]

            # Elements to the left of 'mid' form the left subtree
            root.left = helper(left, mid - 1)
            # Elements to the right of 'mid' form the right subtree
            root.right = helper(mid + 1, right)

            return root

        return helper(0, len(inorder) - 1)