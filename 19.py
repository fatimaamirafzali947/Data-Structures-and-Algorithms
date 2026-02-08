#تابعی بازگشتی بنویسید که مجموع مقادیر تمامی گره‌های یک درخت باینری را محاسبه کند.
def sum_nodes(root):
    if root is None:
        return 0
    return sum_nodes(root.left)+sum_nodes(root.right)+root.values

