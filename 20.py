#تابعی بازگشتی بنویسید که به دنبال target در درختی دودویی بگردد. در صورت یافتن true در غیر این صورت false را در خروجی نشان دهد.
def search (root, target):
    if root is None:
        return False
    if root.value==target:
        return True
    return search (root.left, target) or search (root.right, target)