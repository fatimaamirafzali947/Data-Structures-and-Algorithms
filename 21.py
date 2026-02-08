#تابعی بازگشتی بنویسید که حداکثر داده‌ی درون درخت باینری را بازگرداند.
def max (root):
    if root is None:
        return float('-inf')
    return max (max-t(root.left)), (max-t(root.right)), (root.values)