#درخت BST
def __init__ (self, d):
    self.value=d
    self.Lchild=None
    self.Rchild=None
#تابع بازگشتی یافتن target در درخت BST.
def find_BT (root, target):
    if root is None:
        return False
    if root.values==target:
        return True
    if root.values>target:
        return find_BT(root.Lchild)
    if root.values<target:
        return find_BT(root.Rchild)