class TreeNode:
    """Trinary tree, which generates at its initialisation a n_layers deep tree of circles, given 4 Moebius Transformations."""
    def __init__(self, circle, last_tr, last_tr_inv, oth_tr, oth_tr_inv, n_layers):
        self.circle = circle

        if n_layers != 0:
            self.kid1 = TreeNode(last_tr.dot(circle), last_tr, last_tr_inv, oth_tr, oth_tr_inv, n_layers - 1)
            self.kid2 = TreeNode(oth_tr.dot(circle),  oth_tr, oth_tr_inv, last_tr, last_tr_inv, n_layers - 1)
            self.kid3 = TreeNode(oth_tr_inv.dot(circle), oth_tr_inv, oth_tr, last_tr, last_tr_inv, n_layers - 1)
        else:
            self.kid1 = None
            self.kid2 = None
            self.kid3 = None


    def __iter__(self):
        return TreeIter(self)


    def PrintTree(self):
        """Prints the tree in order (itself before its descendants.)"""
        print(self.circle)
        if self.kid1:
            self.kid1.PrintTree()
        if self.kid2:
            self.kid2.PrintTree()
        if self.kid3:
            self.kid3.PrintTree()



class TreeIter:
    """TreeNode iterator."""
    def __init__(self, TreeNode):
        self.it = self._it_gen(TreeNode)


    def __next__(self):
        try:
            return next(self.it)
        except StopIteration:
            raise StopIteration from None


    def _it_gen(self, tree):
        yield tree.circle

        if tree.kid1 is not None:
            for it in tree.kid1:
                yield it

        if tree.kid2 is not None:
            for it in tree.kid2:
                yield it

        if tree.kid3 is not None:
            for it in tree.kid3:
                yield it

        return
