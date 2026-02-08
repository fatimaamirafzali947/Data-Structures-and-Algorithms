#تابعی بازگشتی بنویسید که با داشتن پیمایش‌های preorder و inorder درخت مورد نظر را بسازد.
def build_tree (preorder, inorder):
    if not preorder or not inorder:
        return None
    value=preorder[0]
    index=inorder.index[val]
    N=tree_nodes(val)
    N.left=build_tree(preorder[1:1+index], inorder[:index])
    N.right=build_tree(preorder[1+index:], inorder[1+index:])