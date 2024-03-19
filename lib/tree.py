class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        if self.root is None:
            return None
        return self._dfs(self.root, id)

    def _dfs(self, node, id):
        # Check if the current node matches the desired id
        if node.get('id') == id:
            return node

        # Traverse children
        for child in node.get('children', []):
            result = self._dfs(child, id)
            if result is not None:
                return result

        return None
