#تابعی بازگشتی بنویسید که درخت را معکوس کند.
def inverse_tree (root):
    if not root:
        return None
    root.left, root.right==root.right, root.left
    inverse_tree(root.left)
    inverse_tree(root.right)